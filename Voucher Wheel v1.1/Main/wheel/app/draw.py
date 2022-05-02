import logging
import math
import random

from django.shortcuts import get_object_or_404

from app.models import UniqueCode, Prize

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Wheel config
NUM_OF_LAPS = 10
NUM_OF_SECTIONS = 15


def calc_wheel_rotations():
    random.seed()
    return math.floor((random.random() * 1440 * NUM_OF_LAPS) + 360)


def get_prize_result(r):
    ps = 360 / NUM_OF_SECTIONS
    return (NUM_OF_SECTIONS - math.ceil((r % 360) / ps)) + 1


def is_code_valid(code) -> bool:
    try:
        ucode = UniqueCode.objects.get(code=code)
        if ucode.used is not True:
            return True
    except Exception as e:
        logger.error(e)
    return False


def set_code_used(code, state):
    try:
        ucode = UniqueCode.objects.get(code=code)
        ucode.used = state
        ucode.save()
    except Exception as e:
        logger.error(e)


def get_prize(pk) -> object:
    try:
        return get_object_or_404(Prize, pk=pk)
    except Exception as e:
        logger.error(e)
    return None
