import csv

# with open('./csv_sample.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # csv_reader = csv.reader(csv_file, delimiter='-')
#     # if delimiter is not comma, you've to explicitly scpecify it
#
#     # next(csv_reader)  # loops over 1st line
#
#     with open('./new_csv_sample.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')  # \t <-- tab delimi
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

with open('./csv_sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line['email'])

    with open('./new_csv_sample.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        # fieldnames = ['first_name', 'last_name']
        # can delete specific column w/ DictWriter

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            # del line['email']  # deletes email column from -o file
            csv_writer.writerow(line)
