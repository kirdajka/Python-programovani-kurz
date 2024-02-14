school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 2],
    ["Chemie", 4],
]
indices = [0,1,2,5]
report_forschool = [school_report[i] for i in indices]
print(report_forschool)
reportschool2= [sublist for sublist in school_report if sublist[1]>3]
print(reportschool2)
sum_of_marks = 0
for mark in report_forschool:
    sum_of_marks += mark[1]
average = sum_of_marks / len(report_forschool)
print(f"Průměrná známka studenta/studentky je {average}.")
