from pathlib import Path
from typing import Union

from pydantic import BaseModel


class SessionPathsModel(BaseModel):
    path_to_session_folder: Union[Path, str] = None
    path_to_synchronized_videos_folder: Union[Path, str] = None
    path_to_calibration_videos_folder: Union[Path, str] = None
    path_to_annotated_videos_folder: Union[Path, str] = None
    path_to_output_data_folder: Union[Path, str] = None
    path_to_folder_of_synchronized_videos: Union[Path, str] = None


class MediaPipe2DParametersModel(BaseModel):
    model_complexity: int = 2
    min_detection_confidence: float = 0.5
    min_tracking_confidence: float = 0.5
    static_image_mode: bool = False


class AniposeTriangulate3DParametersModel(BaseModel):
    anipose_calibration_object: object = None  # I don't wtf that thing is lol
    confidence_threshold_cutoff: float = 0.7
    use_triangulate_ransac_method: bool = True


class ButterworthFilterParametersModel(BaseModel):
    sampling_rate: float = 30
    cutoff_frequency: float = 7
    order: int = 4


class PostProcessingParametersModel(BaseModel):
    framerate: float = 30.0
    butterworth_filter_parameters = ButterworthFilterParametersModel()


class SessionProcessingParameterModel(BaseModel):

    # relevant_paths: SessionPathsModel = SessionPathsModel()
    path_to_session_folder: Union[Path, str] = None
    path_to_synchronized_videos_folder: Union[Path, str] = None
    path_to_calibration_videos_folder: Union[Path, str] = None
    path_to_annotated_videos_folder: Union[Path, str] = None
    path_to_output_data_folder: Union[Path, str] = None
    path_to_folder_of_synchronized_videos: Union[Path, str] = None

    mediapipe_2d_parameters: MediaPipe2DParametersModel = MediaPipe2DParametersModel()

    anipose_triangulate_3d_parameters: AniposeTriangulate3DParametersModel = (
        AniposeTriangulate3DParametersModel()
    )
    post_processing_parameters: PostProcessingParametersModel = (
        PostProcessingParametersModel()
    )
    start_processing_at_stage: Union[int, str] = 0

    class Config:
        arbitrary_types_allowed = True


if __name__ == "__main__":
    import json
    from pprint import pprint
    from pathlib import Path

    session_processing_parameter_model = SessionProcessingParameterModel()
    pprint(session_processing_parameter_model.dict())

    json_path = Path.home() / "freemocap_default_session_parameters.json"
    with open(json_path, "w") as file:
        json_string = json.dumps(session_processing_parameter_model.dict(), indent=4)
        file.write(json_string)

    print(f"Saved to {json_path}")
