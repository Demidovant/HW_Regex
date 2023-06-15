import csv
import re


def format_phone(phone):
    pattern = r"(7|\+7|8)\s*\(?(\d+)\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})((\s*)\(?(доб\.?)\s*(\d+)\)?)?"
    subst_pattern = r"+7(\2)\3-\4-\5\7\8\9"
    return re.sub(pattern, subst_pattern, phone)


result_contacts_list = []
with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    header, *rows = list(rows)
    for row in rows:
        flag = False
        temp_row = ' '.join(row[:3]).split()
        while len(temp_row) < 3:
            temp_row += ['']
        temp_row.extend([*row[3:5], format_phone(row[5]), row[6]])

        if not result_contacts_list:
            result_contacts_list.append(temp_row)
        else:
            for contact in result_contacts_list:
                if temp_row[:2] == contact[:2]:
                    for i in range(2, 7):
                        if temp_row[i] and contact[i] != temp_row[i]:
                            contact[i] = temp_row[i]
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                result_contacts_list.append(temp_row)


with open("phonebook.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerow(header)
    datawriter.writerows(result_contacts_list)
