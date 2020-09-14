#!/usr/bin/env python3

############################################################################
## Author: Frederic Depuydt                                               ##
## Mail: frederic.depuydt@outlook.com                                     ##
############################################################################


from ... import echo

import influxdb

class InfluxDBClient(influxdb.InfluxDBClient):

    def switch_database(self, database: str):
        self.create_database(database)
        super().switch_database(database)