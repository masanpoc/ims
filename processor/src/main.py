import traceback
from config import pg_config

from drivers import PgDriver
from utils.parsers import parse_csv

import json

# TO DO create a class buffer
# to handle duplicates, increase db performance, logging,


class Processor:
    def __init__(self):
        # print(sys.path)
        # print("names from config", dir(config))
        self.pg_driver = PgDriver(pg_config)

    def empty_buffer(self, item_list):
        data_object = {}
        id_list = []

        # parse csv
        for row in item_list:
            parsed_data = parse_csv(row)
            key = parsed_data["key"]
            value = parsed_data["value"]
            data_object[key] = value
            id_list.append(key)

        # input_data = {id1: [val1, val2], id2: [val1, val2]...}
        self.pg_driver.read(id_list)
        self.pg_driver.execute()

        retrieved_ids = []

        # TO DO: move into utils
        for result in self.pg_driver.fetch():
            retrieved_ids.append(result[0])

        output_data = {"insert": [], "update": []}

        # TO DO: use lodash concat or similar but for py
        for item in id_list:
            if item in retrieved_ids:
                data_object[item]["op_mode"] = "U"

            else:
                data_object[item]["op_mode"] = "I"

                # process vals -> (key1, val1, val2, val3)
                insert_values = list(data_object[item].values())
                insert_values.insert(0, item)
                insert_values = tuple(insert_values)

                output_data["insert"].append(insert_values)

        print(json.dumps(output_data, indent=4))

        # conditional based on op_mode

        # if I
        # pg_driver.insert(input_data) [(1, "x"), (2, "y")]
        self.pg_driver.insert(output_data["insert"])
        # elif U
        # self.pg_driver.update(input_data)
        # loop over items in output_data["update"] list
        # else
        # print('not valid input')

        # try to execute
        # output_data = {
        #     insert: [(id1, val1, val2), (id2, val1, val2)],
        #     update: [(..., id3), (..., id4)],
        # }
        # insert(execute_values) commits automatically
        # note: commit after N times executing/updating
        # UPDATE -> update N times [driver.execute(item)]
        # print message if an error occurs

    def init_process(self):
        try:
            input_file = open("clothes.csv", "r")

            # ideally loop over input_file and for each n records -> update DB
            input_file.readline()

            input_data = []

            for line in input_file:
                line = line.strip()
                row = line.split(",")
                input_data.append(row)

                if len(input_data) == 5:
                    self.empty_buffer(input_data)
                    input_data = []

            input_file.close()

        except Exception as e:
            print("Error processing file", e)
            print(traceback.format_exc())


Processor().init_process()
