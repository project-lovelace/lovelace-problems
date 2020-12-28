import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.flight_paths import haversine_distance

logger = logging.getLogger(__name__)

FUNCTION_NAME = "haversine_distance"
INPUT_VARS = ['lat1', 'lon1', 'lat2', 'lon2']
OUTPUT_VARS = ['distance']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'R': 6372.1,  # Radius of the Earth [km]

    'New_York_lat': 40.7128,
    'New_York_lon': -74.0060,
    'Madrid_lat': 40.4168,
    'Madrid_lon': -3.7038,
    'Vancouver_lat': 49.2827,
    'Vancouver_lon': -123.1207,
    'St_Johns_lat': 47.5615,
    'St_Johns_lon': -52.7126,
    'Ushuaia_lat': -54.8019,
    'Ushuaia_lon': -68.3030,
    'Alert_lat': 82.5018,
    'Alert_lon': -62.3481,
    'Dakar_lat': 14.7167,
    'Dakar_lon': -17.4677,
    'Antananarivo_lat': -18.8792,
    'Antananarivo_lon': 47.5079,
    'Rome_lat': 41.9028,
    'Rome_lon': 12.4964,
    'Istanbul_lat': 41.0082,
    'Istanbul_lon': 28.9784,
    'Bengaluru_lat': 12.9716,
    'Bengaluru_lon': 77.5946,
    'Lhasa_lat': 29.6548,
    'Lhasa_lon': 91.1406,
    'Manaus_lat': -3.1190,
    'Manaus_lon': -60.0217,
    'Bandung_lat': -6.9175,
    'Bandung_lon': 107.6191,

    # Eurasian Pole of Inaccessibility or EPIA
    'EPIA_lat': 46.283,
    'EPIA_lon': 86.667,

    # Pacific Pole of Inaccessibility or PPIA
    'PPIA_lat': -48.877,
    'PPIA_lon': -123.393
}
ATOL = {}
RTOL = {
    'distance': 1e-3
}


class TestCaseType(TestCaseTypeEnum):
    SAME_POINT = ("Same point", 1)
    EQUATORIAL = ("Equatorial", 1)
    POLE_TO_POLE = ("Pole to pole", 1)
    NEW_YORK_TO_MADRID = ("New York to Madrid", 1)
    VANCOUVER_TO_ST_JOHNS = ("Vancouver to St. Johns", 1)
    DAKAR_TO_ANTANANARIVO = ("Dakar to Antananarivo", 1)
    ROME_TO_ISTANBUL = ("Rome to Istanbul", 1)
    BENGALURU_TO_LHASA = ("Bengaluru to Lhasa", 1)
    MANAUS_TO_BANDUNG = ("Manaus to Bandung", 1)
    USHUAIA_TO_ALERT = ("Ushuaia to Alert", 1)
    EPIA_TO_PPIA = ("Eurasian Pole of Inaccessibility to Pacific Pole of Inaccessibility", 1)
    RANDOM_POINTS = ("Two random points", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['lat1'], self.input['lon1'], self.input['lat2'], self.input['lon2']

    def output_tuple(self) -> tuple:
        return self.output['distance'],

    def output_str(self) -> str:
        return str(self.output['distance'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.SAME_POINT:
        lat1 = uniform(-90, 90)
        lon1 = uniform(-180, 180)
        lat2 = lat1
        lon2 = lon1

    if test_type is TestCaseType.EQUATORIAL:
        lat1 = 0
        lon1 = uniform(-180, 180)
        lat2 = 0
        lon2 = uniform(-180, 180)

    if test_type is TestCaseType.POLE_TO_POLE:
        lat1 = 90
        lon1 = uniform(-180, 180)
        lat2 = -90
        lon2 = uniform(-180, 180)

    if test_type is TestCaseType.NEW_YORK_TO_MADRID:
        lat1 = PHYSICAL_CONSTANTS['New_York_lat']
        lon1 = PHYSICAL_CONSTANTS['New_York_lon']
        lat2 = PHYSICAL_CONSTANTS['Madrid_lat']
        lon2 = PHYSICAL_CONSTANTS['Madrid_lon']

    if test_type is TestCaseType.VANCOUVER_TO_ST_JOHNS:
        lat1 = PHYSICAL_CONSTANTS['Vancouver_lat']
        lon1 = PHYSICAL_CONSTANTS['Vancouver_lon']
        lat2 = PHYSICAL_CONSTANTS['St_Johns_lat']
        lon2 = PHYSICAL_CONSTANTS['St_Johns_lon']

    if test_type is TestCaseType.DAKAR_TO_ANTANANARIVO:
        lat1 = PHYSICAL_CONSTANTS['Dakar_lat']
        lon1 = PHYSICAL_CONSTANTS['Dakar_lon']
        lat2 = PHYSICAL_CONSTANTS['Antananarivo_lat']
        lon2 = PHYSICAL_CONSTANTS['Antananarivo_lon']

    if test_type is TestCaseType.ROME_TO_ISTANBUL:
        lat1 = PHYSICAL_CONSTANTS['Rome_lat']
        lon1 = PHYSICAL_CONSTANTS['Rome_lon']
        lat2 = PHYSICAL_CONSTANTS['Istanbul_lat']
        lon2 = PHYSICAL_CONSTANTS['Istanbul_lon']

    if test_type is TestCaseType.BENGALURU_TO_LHASA:
        lat1 = PHYSICAL_CONSTANTS['Bengaluru_lat']
        lon1 = PHYSICAL_CONSTANTS['Bengaluru_lon']
        lat2 = PHYSICAL_CONSTANTS['Lhasa_lat']
        lon2 = PHYSICAL_CONSTANTS['Lhasa_lon']

    if test_type is TestCaseType.MANAUS_TO_BANDUNG:
        lat1 = PHYSICAL_CONSTANTS['Manaus_lat']
        lon1 = PHYSICAL_CONSTANTS['Manaus_lon']
        lat2 = PHYSICAL_CONSTANTS['Bandung_lat']
        lon2 = PHYSICAL_CONSTANTS['Bandung_lon']

    if test_type is TestCaseType.USHUAIA_TO_ALERT:
        lat1 = PHYSICAL_CONSTANTS['Ushuaia_lat']
        lon1 = PHYSICAL_CONSTANTS['Ushuaia_lon']
        lat2 = PHYSICAL_CONSTANTS['Alert_lat']
        lon2 = PHYSICAL_CONSTANTS['Alert_lon']

    if test_type is TestCaseType.EPIA_TO_PPIA:
        lat1 = PHYSICAL_CONSTANTS['EPIA_lat']
        lon1 = PHYSICAL_CONSTANTS['EPIA_lon']
        lat2 = PHYSICAL_CONSTANTS['PPIA_lat']
        lon2 = PHYSICAL_CONSTANTS['PPIA_lon']

    if test_type is TestCaseType.RANDOM_POINTS:
        lat1 = uniform(-90, 90)
        lon1 = uniform(-180, 180)
        lat2 = uniform(-90, 90)
        lon2 = uniform(-180, 180)

    test_case.input = {
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }

    test_case.output['distance'] = haversine_distance(lat1, lon1, lat2, lon2)

    return test_case
