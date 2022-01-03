
from gi.repository import GObject


ENCODING_CATEGORY_CAPTURE: str = ...
ENCODING_CATEGORY_DEVICE: str = ...
ENCODING_CATEGORY_FILE_EXTENSION: str = ...
ENCODING_CATEGORY_ONLINE_SERVICE: str = ...
ENCODING_CATEGORY_STORAGE_EDITING: str = ...
PLUGINS_BASE_VERSION_MAJOR: int = ...
PLUGINS_BASE_VERSION_MICRO: int = ...
PLUGINS_BASE_VERSION_MINOR: int = ...
PLUGINS_BASE_VERSION_NANO = ...
_namespace: str = ...
_version: str = ...

def codec_utils_aac_caps_set_level_and_profile(*args, **kwargs): ...
def codec_utils_aac_get_channels(*args, **kwargs): ...
def codec_utils_aac_get_index_from_sample_rate(*args, **kwargs): ...
def codec_utils_aac_get_level(*args, **kwargs): ...
def codec_utils_aac_get_profile(*args, **kwargs): ...
def codec_utils_aac_get_sample_rate(*args, **kwargs): ...
def codec_utils_aac_get_sample_rate_from_index(*args, **kwargs): ...
def codec_utils_h264_caps_set_level_and_profile(*args, **kwargs): ...
def codec_utils_h264_get_level(*args, **kwargs): ...
def codec_utils_h264_get_level_idc(*args, **kwargs): ...
def codec_utils_h264_get_profile(*args, **kwargs): ...
def codec_utils_h265_caps_set_level_tier_and_profile(*args, **kwargs): ...
def codec_utils_h265_get_level(*args, **kwargs): ...
def codec_utils_h265_get_level_idc(*args, **kwargs): ...
def codec_utils_h265_get_profile(*args, **kwargs): ...
def codec_utils_h265_get_tier(*args, **kwargs): ...
def codec_utils_mpeg4video_caps_set_level_and_profile(*args, **kwargs): ...
def codec_utils_mpeg4video_get_level(*args, **kwargs): ...
def codec_utils_mpeg4video_get_profile(*args, **kwargs): ...
def codec_utils_opus_create_caps(*args, **kwargs): ...
def codec_utils_opus_create_caps_from_header(*args, **kwargs): ...
def codec_utils_opus_create_header(*args, **kwargs): ...
def codec_utils_opus_parse_caps(*args, **kwargs): ...
def codec_utils_opus_parse_header(*args, **kwargs): ...
def encoding_list_all_targets(*args, **kwargs): ...
def encoding_list_available_categories(*args, **kwargs): ...
def install_plugins_async(*args, **kwargs): ...
def install_plugins_installation_in_progress(*args, **kwargs): ...
def install_plugins_return_get_name(*args, **kwargs): ...
def install_plugins_supported(*args, **kwargs): ...
def install_plugins_sync(*args, **kwargs): ...
def is_missing_plugin_message(*args, **kwargs): ...
def missing_decoder_installer_detail_new(*args, **kwargs): ...
def missing_decoder_message_new(*args, **kwargs): ...
def missing_element_installer_detail_new(*args, **kwargs): ...
def missing_element_message_new(*args, **kwargs): ...
def missing_encoder_installer_detail_new(*args, **kwargs): ...
def missing_encoder_message_new(*args, **kwargs): ...
def missing_plugin_message_get_description(*args, **kwargs): ...
def missing_plugin_message_get_installer_detail(*args, **kwargs): ...
def missing_uri_sink_installer_detail_new(*args, **kwargs): ...
def missing_uri_sink_message_new(*args, **kwargs): ...
def missing_uri_source_installer_detail_new(*args, **kwargs): ...
def missing_uri_source_message_new(*args, **kwargs): ...
def pb_utils_add_codec_description_to_tag_list(*args, **kwargs): ...
def pb_utils_get_codec_description(*args, **kwargs): ...
def pb_utils_get_decoder_description(*args, **kwargs): ...
def pb_utils_get_element_description(*args, **kwargs): ...
def pb_utils_get_encoder_description(*args, **kwargs): ...
def pb_utils_get_sink_description(*args, **kwargs): ...
def pb_utils_get_source_description(*args, **kwargs): ...
def pb_utils_init(*args, **kwargs): ...
def plugins_base_version(*args, **kwargs): ...
def plugins_base_version_string(*args, **kwargs): ...

class AudioVisualizer:
    ainfo = ...
    priv = ...
    req_spf = ...
    vinfo = ...
    
    def do_decide_allocation(self, *args, **kwargs): ...
    def do_render(self, *args, **kwargs): ...
    def do_setup(self, *args, **kwargs): ...
    

class Discoverer:
    _reserved = ...
    parent = ...
    priv = ...
    
    def discover_uri(self, uri: str) -> DiscovererInfo: ...
    def discover_uri_async(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def start(*args, **kwargs): ...
    def stop(*args, **kwargs): ...
    
    def do_discovered(self, *args, **kwargs): ...
    def do_finished(self, *args, **kwargs): ...
    def do_source_setup(self, *args, **kwargs): ...
    def do_starting(self, *args, **kwargs): ...
    

class DiscovererAudioInfo:
    def get_bitrate(*args, **kwargs): ...
    def get_channel_mask(*args, **kwargs): ...
    def get_channels(*args, **kwargs): ...
    def get_depth(*args, **kwargs): ...
    def get_language(*args, **kwargs): ...
    def get_max_bitrate(*args, **kwargs): ...
    def get_sample_rate(*args, **kwargs): ...
    

class DiscovererContainerInfo:
    def get_streams(*args, **kwargs): ...


class DiscovererInfo:
    def copy(*args, **kwargs): ...
    def from_variant(*args, **kwargs): ...
    def get_audio_streams(self) -> list[DiscovererStreamInfo]: ...
    def get_container_streams(*args, **kwargs): ...
    def get_duration(*args, **kwargs): ...
    def get_live(*args, **kwargs): ...
    def get_misc(*args, **kwargs): ...
    def get_missing_elements_installer_details(*args, **kwargs): ...
    def get_result(*args, **kwargs): ...
    def get_seekable(*args, **kwargs): ...
    def get_stream_info(*args, **kwargs): ...
    def get_stream_list(*args, **kwargs): ...
    def get_streams(*args, **kwargs): ...
    def get_subtitle_streams(*args, **kwargs): ...
    def get_tags(*args, **kwargs): ...
    def get_toc(*args, **kwargs): ...
    def get_uri(*args, **kwargs): ...
    def get_video_streams(*args, **kwargs): ...
    def to_variant(*args, **kwargs): ...
    

class DiscovererStreamInfo:
    def get_caps(*args, **kwargs): ...
    def get_misc(*args, **kwargs): ...
    def get_next(*args, **kwargs): ...
    def get_previous(*args, **kwargs): ...
    def get_stream_id(*args, **kwargs): ...
    def get_stream_type_nick(*args, **kwargs): ...
    def get_tags(*args, **kwargs): ...
    def get_toc(*args, **kwargs): ...
    def list_free(*args, **kwargs): ...
    

class DiscovererSubtitleInfo:
    def get_language(*args, **kwargs): ...
    

class DiscovererVideoInfo:
    def get_bitrate(*args, **kwargs): ...
    def get_depth(*args, **kwargs): ...
    def get_framerate_denom(*args, **kwargs): ...
    def get_framerate_num(*args, **kwargs): ...
    def get_height(*args, **kwargs): ...
    def get_max_bitrate(*args, **kwargs): ...
    def get_par_denom(*args, **kwargs): ...
    def get_par_num(*args, **kwargs): ...
    def get_width(*args, **kwargs): ...
    def is_image(*args, **kwargs): ...
    def is_interlaced(*args, **kwargs): ...
    

class EncodingAudioProfile:
    def new(*args, **kwargs): ...
    

class EncodingContainerProfile:
    def add_profile(*args, **kwargs): ...
    def contains_profile(*args, **kwargs): ...
    def get_profiles(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    

class EncodingProfile:
    def copy(*args, **kwargs): ...
    def find(*args, **kwargs): ...
    def from_discoverer(*args, **kwargs): ...
    def get_allow_dynamic_output(*args, **kwargs): ...
    def get_description(*args, **kwargs): ...
    def get_file_extension(*args, **kwargs): ...
    def get_format(*args, **kwargs): ...
    def get_input_caps(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_presence(*args, **kwargs): ...
    def get_preset(*args, **kwargs): ...
    def get_preset_name(*args, **kwargs): ...
    def get_restriction(*args, **kwargs): ...
    def get_single_segment(*args, **kwargs): ...
    def get_type_nick(*args, **kwargs): ...
    def is_enabled(*args, **kwargs): ...
    def is_equal(*args, **kwargs): ...
    def set_allow_dynamic_output(*args, **kwargs): ...
    def set_description(*args, **kwargs): ...
    def set_enabled(*args, **kwargs): ...
    def set_format(*args, **kwargs): ...
    def set_name(*args, **kwargs): ...
    def set_presence(*args, **kwargs): ...
    def set_preset(*args, **kwargs): ...
    def set_preset_name(*args, **kwargs): ...
    def set_restriction(*args, **kwargs): ...
    def set_single_segment(*args, **kwargs): ...
    

class EncodingTarget:
    def add_profile(*args, **kwargs): ...
    def get_category(*args, **kwargs): ...
    def get_description(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_path(*args, **kwargs): ...
    def get_profile(*args, **kwargs): ...
    def get_profiles(*args, **kwargs): ...
    def load(*args, **kwargs): ...
    def load_from_file(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def save(*args, **kwargs): ...
    def save_to_file(*args, **kwargs): ...
    

class EncodingVideoProfile:
    def get_pass(*args, **kwargs): ...
    def get_variableframerate(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_pass(*args, **kwargs): ...
    def set_variableframerate(*args, **kwargs): ...
    

class InstallPluginsContext:
    def free(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_confirm_search(*args, **kwargs): ...
    def set_desktop_id(*args, **kwargs): ...
    def set_startup_notification_id(*args, **kwargs): ...
    def set_xid(*args, **kwargs): ...
    

class DiscovererSerializeFlags(GObject.GFlags):
    BASIC = ...
    CAPS = ...
    TAGS = ...
    MISC = ...
    ALL = ...

class AudioVisualizerShader(GObject.GEnum):
    NONE = ...
    FADE = ...
    FADE_AND_MOVE_UP = ...
    FADE_AND_MOVE_DOWN = ...
    FADE_AND_MOVE_LEFT = ...
    FADE_AND_MOVE_RIGHT = ...
    FADE_AND_MOVE_HORIZ_OUT = ...
    FADE_AND_MOVE_HORIZ_IN = ...
    FADE_AND_MOVE_VERT_OUT = ...
    FADE_AND_MOVE_VERT_IN = ...

class DiscovererResult(GObject.GEnum):
    OK = ...
    URI_INVALID = ...
    ERROR = ...
    TIMEOUT = ...
    BUSY = ...
    MISSING_PLUGINS = ...

class InstallPluginsReturn(GObject.GEnum):
    SUCCESS = ...
    NOT_FOUND = ...
    ERROR = ...
    PARTIAL_SUCCESS = ...
    USER_ABORT = ...
    CRASHED = ...
    INVALID = ...
    STARTED_OK = ...
    INTERNAL_FAILURE = ...
    HELPER_MISSING = ...
    INSTALL_IN_PROGRESS = ...
    get_name = ...