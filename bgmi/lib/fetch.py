from bgmi.config import DATA_SOURCE
from bgmi.utils import print_error
from bgmi.website import bangumi_moe, mikan, share_dmhy

DATA_SOURCE_MAP = {
    "mikan_project": mikan.Mikanani,
    "bangumi_moe": bangumi_moe.BangumiMoe,
    "dmhy": share_dmhy.DmhySource,
}


try:
    website = DATA_SOURCE_MAP[DATA_SOURCE]()
except KeyError:
    print_error(
        'date source "{}" in config is wrong, please edit it manually'.format(
            DATA_SOURCE
        )
    )
