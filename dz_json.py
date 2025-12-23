import json


def generate_report(json_file_path):

    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)


    report = {}

    for task in data:
        assignee = task['assignee']
        if task['status'] == 'completed':

            if assignee not in report:
                report[assignee] = 0


            report[assignee] += 1

    return report


#
if __name__ == "__main__":
    result = generate_report('tasks.json')
    print(result)