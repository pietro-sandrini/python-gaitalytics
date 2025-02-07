from pathlib import Path

from gaitalytics import api
from gaitalytics import c3d_reader
from gaitalytics import model
from gaitalytics import utils


def main():
    settings_file = "settings/hbm_pig.yaml"
    file_path = "./tests/data/Baseline.5.c3d"
    buffered_path_raw = Path("./out/raw.h5")
    buffered_path_norm = Path("./out/raw.h5")

    configs = utils.ConfigProvider(settings_file)
    if not buffered_path_raw.exists():
        buffered_path_raw.parent.mkdir(parents=True, exist_ok=True)
        cycle_data = api.extract_cycles(
            file_path, configs, buffer_output_path=buffered_path_raw, file_handler_class=c3d_reader.BtkFileHandler
        )
    else:
        cycle_data = api.extract_cycles_buffered(buffered_path_raw, configs)[model.ExtractedCycleDataCondition.RAW_DATA]

    api.normalise_cycles(configs, cycle_data, buffer_output_path=buffered_path_norm)


# __name__
if __name__ == "__main__":
    main()
