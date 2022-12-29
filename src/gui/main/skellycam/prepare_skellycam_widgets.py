from PyQt6.QtWidgets import QDockWidget, QWidget
from skellycam import (
    SkellyCamControllerWidget,
    SkellyCamParameterTreeWidget,
    SkellyCamViewerWidget,
)


def prepare_skellycam_widgets(parent: QWidget = None):
    skellycam_viewer_widget = SkellyCamViewerWidget(
        session_folder_path=None,
        parent=parent,
    )

    skellycam_controller_dock_widget = QDockWidget("Camera Controller", parent)
    skellycam_controller_widget = SkellyCamControllerWidget(
        qt_multi_camera_viewer_widget=skellycam_viewer_widget,
        parent=parent,
    )

    skellycam_controller_dock_widget.setWidget(skellycam_controller_widget)

    skellycam_parameter_tree_widget = SkellyCamParameterTreeWidget()

    # connect signals to slots
    skellycam_viewer_widget.camera_group_created_signal.connect(
        skellycam_parameter_tree_widget.update_camera_config_parameter_tree
    )

    skellycam_parameter_tree_widget.emitting_camera_configs_signal.connect(
        skellycam_viewer_widget.incoming_camera_configs_signal
    )

    return (
        skellycam_viewer_widget,
        skellycam_controller_dock_widget,
        skellycam_parameter_tree_widget,
    )
