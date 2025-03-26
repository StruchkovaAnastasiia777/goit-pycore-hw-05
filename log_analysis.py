import sys
from collections import defaultdict
from typing import List, Dict

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Розбирає рядок логу та повертає його у вигляді словника з датою, часом, рівнем та повідомленням.

    Аргументи:
    - line: Рядок логу, який потрібно розібрати.

    Повертає:
    - Словник, що містить 'date', 'time', 'level' та 'message'.
    """
    try:
        parts = line.split(maxsplit=3)
        return {
            'date': parts[0],
            'time': parts[1],
            'level': parts[2],
            'message': parts[3].strip()
        }
    except IndexError:
        print(f"Warning: incorrect log line format: {line.strip()}")
        return {}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує логи з файлу та розбирає їх.

    Аргументи:
    - file_path: Шлях до файлу, що містить логи.

    Повертає:
    - Список словників, де кожен словник містить 'date', 'time', 'level' та 'message'.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує логи за рівнем (INFO, DEBUG, ERROR, WARNING).

    Аргументи:
    - logs: Список логів.
    - level: Рівень логу, за яким буде здійснено фільтрацію.

    Повертає:
    - Список логів, що відповідають заданому рівню.
    """
    return [log for log in logs if log['level'] == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість логів для кожного рівня.

    Аргументи:
    - logs: Список логів.

    Повертає:
    - Словник, де ключами є рівні логу, а значеннями — кількість таких логів.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Виводить кількість логів для кожного рівня.

    Аргументи:
    - counts: Словник з кількістю логів для кожного рівня.
    """
    print("Log Level | Count")
    print("-----------|-------")
    for level, count in counts.items():
        print(f"{level:<11} | {count}")

def display_filtered_logs(logs: List[Dict[str, str]]):
    """
    Виводить логи, які відповідають заданим критеріям.

    Аргументи:
    - logs: Список логів для відображення.
    """
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    file_path = '/Users/anastasiiajaguzhinskaya/logfile.log'
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_file> [level]")
        print("Available levels: INFO, DEBUG, ERROR, WARNING")
        sys.exit(1)
    
    logs = load_logs(file_path)
    
    if not logs:
        print("Log file is empty or contains invalid data.")
        sys.exit(1)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        if level not in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
            print(f"Invalid log level: {level}")
            sys.exit(1)
            
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"Log details for level '{level}':")
        display_filtered_logs(filtered_logs)
