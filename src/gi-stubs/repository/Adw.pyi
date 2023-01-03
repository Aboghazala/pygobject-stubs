from gi.repository import Gtk, GObject, Gdk, Gio, GLib

from typing import Union

DURATION_INFINITE: int = ...
MAJOR_VERSION: int = ...
MICRO_VERSION = ...
MINOR_VERSION: int = ...
VERSION_S: str = ...
_lock = ...
_namespace: str = ...
_version: str = ...

def easing_ease(value: float) -> float: ...
def get_enable_animations(widget: Gtk.Widget) -> bool: ...
def get_major_version() -> int: ...
def get_micro_version() -> int: ...
def get_minor_version() -> int: ...
def init() -> None: ...
def is_initialized() -> bool: ...
def lerp(a: float, b: float, t: float) -> float: ...

class AboutWindow:
    def add_acknowledgement_section(*args, **kwargs): ...
    def add_credit_section(*args, **kwargs): ...
    def add_legal_section(*args, **kwargs): ...
    def add_link(*args, **kwargs): ...
    def get_application_icon(*args, **kwargs): ...
    def get_application_name(*args, **kwargs): ...
    def get_artists(*args, **kwargs): ...
    def get_comments(*args, **kwargs): ...
    def get_copyright(*args, **kwargs): ...
    def get_debug_info(*args, **kwargs): ...
    def get_debug_info_filename(*args, **kwargs): ...
    def get_designers(*args, **kwargs): ...
    def get_developer_name(*args, **kwargs): ...
    def get_developers(*args, **kwargs): ...
    def get_documenters(*args, **kwargs): ...
    def get_issue_url(*args, **kwargs): ...
    def get_license(*args, **kwargs): ...
    def get_license_type(*args, **kwargs): ...
    def get_release_notes(*args, **kwargs): ...
    def get_release_notes_version(*args, **kwargs): ...
    def get_support_url(*args, **kwargs): ...
    def get_translator_credits(*args, **kwargs): ...
    def get_version(*args, **kwargs): ...
    def get_website(*args, **kwargs): ...
    def set_application_icon(*args, **kwargs): ...
    def set_application_name(*args, **kwargs): ...
    def set_artists(*args, **kwargs): ...
    def set_comments(*args, **kwargs): ...
    def set_copyright(*args, **kwargs): ...
    def set_debug_info(*args, **kwargs): ...
    def set_debug_info_filename(*args, **kwargs): ...
    def set_designers(*args, **kwargs): ...
    def set_developer_name(*args, **kwargs): ...
    def set_developers(*args, **kwargs): ...
    def set_documenters(*args, **kwargs): ...
    def set_issue_url(*args, **kwargs): ...
    def set_license(*args, **kwargs): ...
    def set_license_type(*args, **kwargs): ...
    def set_release_notes(*args, **kwargs): ...
    def set_release_notes_version(*args, **kwargs): ...
    def set_support_url(*args, **kwargs): ...
    def set_translator_credits(*args, **kwargs): ...
    def set_version(*args, **kwargs): ...
    def set_website(*args, **kwargs): ...

class ActionRow:
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_suffix(self, widget: Gtk.Widget) -> None: ...
    def get_activatable_widget(self) -> Union[Gtk.Widget, None]: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_subtitle(self) -> Union[str, None]: ...
    def get_subtitle_lines(self) -> int: ...
    def get_title_lines(self) -> int: ...
    def remove(self, widget: Gtk.Widget) -> None: ...
    def set_activatable_widget(self, widget: Union[Gtk.Widget, None]) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_subtitle_lines(self, subtitle_lines: int) -> None: ...
    def set_title_lines(self, title_lines: int) -> None: ...

class Animation:
    parent_instance: GObject.Object = ...

    def get_state(self) -> AnimationState: ...
    def get_target(self) -> AnimationTarget: ...
    def get_value(self) -> float: ...
    def get_widget() -> Gtk.Widget: ...
    def pause(self) -> None: ...
    def play(self) -> None: ...
    def reset(self) -> None: ...
    def resume(self) -> None: ...
    def set_target(*args, **kwargs): ...
    def skip(self) -> None: ...

class AnimationTarget: ...

class Application:
    def get_style_manager(self) -> StyleManager: ...

class ApplicationWindow:
    def get_content(self) -> Gtk.Widget: ...
    def set_content(self, widget: Union[Gtk.Widget, None]) -> None: ...

class Avatar:
    def draw_to_texture(scale_factor: int) -> Gdk.Texture: ...
    def get_custom_image(self) -> Union[Gdk.Paintable, None]: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_show_initials(self) -> bool: ...
    def get_text(self) -> Union[str, None]: ...
    @classmethod
    def new(size: int, text: Union[str, None], show_initials: bool) -> Gtk.Widget: ...
    def set_custom_image(self, custom_image: Union[Gdk.Paintable, None]) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_show_initials(self, show_initials: bool) -> None: ...
    def set_size(self, size: int) -> None: ...
    def set_text(self, text: Union[str, None]) -> None: ...

class Bin:
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...

class ButtonContent:
    def get_icon_name(self) -> str: ...
    def get_label(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class CallbackAnimationTarget:
    @classmethod
    def new(callback: Union[AnimationTargetFunc, None]) -> AnimationTarget: ...

class Carousel:
    def append(self, child: Gtk.Widget) -> None: ...
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_allow_scroll_wheel(self) -> bool: ...
    def get_interactive(self) -> bool: ...
    def get_n_pages(self) -> int: ...
    def get_nth_page(self, n: int) -> Gtk.Widget: ...
    def get_position(self) -> float: ...
    def get_reveal_duration(self) -> int: ...
    def get_scroll_params(self) -> SpringParams: ...
    def get_spacing(self) -> int: ...
    def insert(self, child: Gtk.Widget, position: int) -> None: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def prepend(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder(self, child: Gtk.Widget, position: int) -> None: ...
    def scroll_to(self, widget: Gtk.Widget, animate: bool) -> None: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_allow_scroll_wheel(self, allow_scroll_wheel: bool) -> None: ...
    def set_interactive(self, interactive: bool) -> None: ...
    def set_reveal_duration(self, reveal_duration: int) -> None: ...
    def set_scroll_params(self, params: SpringParams) -> None: ...
    def set_spacing(self, spacing: int) -> None: ...

class CarouselIndicatorDots:
    def get_carousel(self) -> Union[Carousel, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_carousel(self, carousel: Union[Carousel, None]) -> None: ...

class CarouselIndicatorLines:
    def get_carousel(self) -> Union[Carousel, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_carousel(self, carousel: Union[Carousel, None]) -> None: ...

class Clamp:
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampLayout:
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ClampScrollable:
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    def get_maximum_size(self) -> int: ...
    def get_tightening_threshold(self) -> int: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...
    def set_maximum_size(self, maximum_size: int) -> None: ...
    def set_tightening_threshold(self, tightening_threshold: int) -> None: ...

class ComboRow:
    def get_expression(self) -> Gtk.Expression: ...
    def get_factory(self) -> Union[Gtk.ListItemFactory, None]: ...
    def get_list_factory(self) -> Union[Gtk.ListItemFactory, None]: ...
    def get_model(self) -> Union[Gio.ListModel, None]: ...
    def get_selected(self) -> int: ...
    def get_selected_item(self) -> Union[GObject.Object, None]: ...
    def get_use_subtitle(self) -> bool: ...
    def set_expression(self, expression: Union[Gtk.Expression, None]) -> None: ...
    def set_factory(self, factory: Union[Gtk.ListItemFactory, None]) -> None: ...
    def set_list_factory(self, factory: Union[Gtk.ListItemFactory, None]) -> None: ...
    def set_model(self, model: Union[Gio.ListModel, None]) -> None: ...
    def set_selected(self, position: int) -> None: ...
    def set_use_subtitle(self, use_subtitle: bool) -> None: ...

class EntryRow:
    def add_prefix(*args, **kwargs): ...
    def add_suffix(*args, **kwargs): ...
    def get_activates_default(*args, **kwargs): ...
    def get_attributes(*args, **kwargs): ...
    def get_enable_emoji_completion(*args, **kwargs): ...
    def get_input_hints(*args, **kwargs): ...
    def get_input_purpose(*args, **kwargs): ...
    def get_show_apply_button(*args, **kwargs): ...
    def remove(*args, **kwargs): ...
    def set_activates_default(*args, **kwargs): ...
    def set_attributes(*args, **kwargs): ...
    def set_enable_emoji_completion(*args, **kwargs): ...
    def set_input_hints(*args, **kwargs): ...
    def set_input_purpose(*args, **kwargs): ...
    def set_show_apply_button(*args, **kwargs): ...

class EnumListItem:
    def get_name(self) -> str: ...
    def get_nick(self) -> str: ...
    def get_value(self) -> int: ...

class EnumListModel:
    def find_position(self, value: int) -> int: ...
    def get_enum_type(self) -> GObject.GType: ...
    @classmethod
    def new(enum_type: GObject.GType) -> EnumListModel: ...

class ExpanderRow:
    def add_action(self, widget: Gtk.Widget) -> None: ...
    def add_prefix(self, widget: Gtk.Widget) -> None: ...
    def add_row(self, child: Gtk.Widget) -> None: ...
    def get_enable_expansion(self) -> bool: ...
    def get_expanded(self) -> bool: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_show_enable_switch(self) -> bool: ...
    def get_subtitle(self) -> str: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_enable_expansion(self, enable_expansion: bool) -> None: ...
    def set_expanded(self, expanded: bool) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_show_enable_switch(self, show_enable_switch: bool) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...

class Flap:
    def get_content(self) -> Union[Gtk.Widget, None]: ...
    def get_flap(self) -> Union[Gtk.Widget, None]: ...
    def get_flap_position(self) -> Gtk.PackType: ...
    def get_fold_duration(self) -> int: ...
    def get_fold_policy(self) -> FlapFoldPolicy: ...
    def get_fold_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_folded(self) -> bool: ...
    def get_locked(self) -> bool: ...
    def get_modal(self) -> bool: ...
    def get_reveal_flap(self) -> bool: ...
    def get_reveal_params(self) -> SpringParams: ...
    def get_reveal_progress(self) -> float: ...
    def get_separator(self) -> Union[Gtk.Widget, None]: ...
    def get_swipe_to_close(self) -> bool: ...
    def get_swipe_to_open(self) -> bool: ...
    def get_transition_type(self) -> FlapTransitionType: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_content(self, content: Union[Gtk.Widget, None]) -> None: ...
    def set_flap(self, flap: Union[Gtk.Widget, None]) -> None: ...
    def set_flap_position(self, position: Gtk.PackType) -> None: ...
    def set_fold_duration(self, duration: int) -> None: ...
    def set_fold_policy(self, policy: FlapFoldPolicy) -> None: ...
    def set_fold_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_locked(self, locked: bool) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_reveal_flap(self, reveal_flap: bool) -> None: ...
    def set_reveal_params(self, params: SpringParams) -> None: ...
    def set_separator(self, separator: Union[Gtk.Widget, None]): ...
    def set_swipe_to_close(self, swipe_to_close: bool) -> None: ...
    def set_swipe_to_open(self, swipe_to_open: bool) -> None: ...
    def set_transition_type(self, transition_type: FlapTransitionType) -> None: ...

class HeaderBar:
    def get_centering_policy(self) -> CenteringPolicy: ...
    def get_decoration_layout(self) -> Union[str, None]: ...
    def get_show_end_title_buttons(self) -> bool: ...
    def get_show_start_title_buttons(self) -> bool: ...
    def get_title_widget(self) -> Union[Gtk.Widget, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def pack_end(self, child: Gtk.Widget) -> None: ...
    def pack_start(self, child: Gtk.Widget) -> None: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_centering_policy(self, centering_policy: CenteringPolicy) -> None: ...
    def set_decoration_layout(self, layout: Union[str, None]) -> None: ...
    def set_show_end_title_buttons(self, setting: bool) -> None: ...
    def set_show_start_title_buttons(self, setting: bool) -> None: ...
    def set_title_widget(self, title_widget: Union[Gtk.Widget, None]) -> None: ...

class Leaflet:
    def append(self, child: Gtk.Widget) -> LeafletPage: ...
    def get_adjacent_child(
        self, direction: NavigationDirection
    ) -> Union[Gtk.Widget, None]: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_can_navigate_forward(self) -> bool: ...
    def get_can_unfold(self) -> bool: ...
    def get_child_by_name(self, name: str) -> Union[Gtk.Widget, None]: ...
    def get_child_transition_params(self) -> SpringParams: ...
    def get_child_transition_running(self) -> bool: ...
    def get_fold_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_folded(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_mode_transition_duration(self) -> int: ...
    def get_page(self, child: Gtk.Widget) -> Leaflet: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_transition_type(self) -> LeafletTransitionType: ...
    def get_visible_child(self) -> Union[Gtk.Widget, None]: ...
    def get_visible_child_name(self) -> Union[str, None]: ...
    def insert_child_after(
        self, child: Gtk.Widget, sibling: Union[Gtk.Widget, None]
    ) -> LeafletPage: ...
    def navigate(self, direction: NavigationDirection) -> bool: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def prepend(self, child: Gtk.Widget) -> LeafletPage: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def reorder_child_after(
        self, child: Gtk.Widget, sibling: Union[Gtk.Widget, None]
    ) -> None: ...
    def set_can_navigate_back(self, can_navigate_back: bool) -> None: ...
    def set_can_navigate_forward(self, can_navigate_forward: bool) -> None: ...
    def set_can_unfold(self, can_unfold: bool) -> None: ...
    def set_child_transition_params(self, params: SpringParams) -> None: ...
    def set_fold_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_mode_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: LeafletTransitionType) -> None: ...
    def set_visible_child(self, visible_child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class LeafletPage:
    def get_child(self) -> Gtk.Widget: ...
    def get_name(self) -> Union[str, None]: ...
    def get_navigatable(self) -> bool: ...
    def set_name(self, name: Union[str, None]) -> None: ...
    def set_navigatable(self, navigatable: bool) -> None: ...

class MessageDialog:
    def add_response(*args, **kwargs): ...
    def get_body(*args, **kwargs): ...
    def get_body_use_markup(*args, **kwargs): ...
    def get_close_response(*args, **kwargs): ...
    def get_default_response(*args, **kwargs): ...
    def get_extra_child(*args, **kwargs): ...
    def get_heading(*args, **kwargs): ...
    def get_heading_use_markup(*args, **kwargs): ...
    def get_response_appearance(*args, **kwargs): ...
    def get_response_enabled(*args, **kwargs): ...
    def get_response_label(*args, **kwargs): ...
    def has_response(*args, **kwargs): ...
    def response(*args, **kwargs): ...
    def set_body(*args, **kwargs): ...
    def set_body_use_markup(*args, **kwargs): ...
    def set_close_response(*args, **kwargs): ...
    def set_default_response(*args, **kwargs): ...
    def set_extra_child(*args, **kwargs): ...
    def set_heading(*args, **kwargs): ...
    def set_heading_use_markup(*args, **kwargs): ...
    def set_response_appearance(*args, **kwargs): ...
    def set_response_enabled(*args, **kwargs): ...
    def set_response_label(*args, **kwargs): ...
    def do_response(self, *args, **kwargs): ...

class PasswordEntryRow: ...

class PreferencesGroup:
    def add(self, child: Gtk.Widget) -> None: ...
    def get_description(self) -> Union[str, None]: ...
    def get_header_suffix(self) -> Union[Gtk.Widget, None]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_description(self, description: Union[str, None]) -> None: ...
    def set_header_suffix(self, suffix: Union[Gtk.Widget, None]) -> None: ...
    def set_title(self, title: str) -> None: ...

class PreferencesPage:
    def add(self, group: PreferencesGroup) -> None: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_title(self) -> str: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def remove(self, group: PreferencesGroup) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_use_underline(self, user_underline: bool) -> None: ...

class PreferencesRow:
    def get_title(self) -> str: ...
    def get_title_selectable(self) -> bool: ...
    def get_use_markup(self) -> bool: ...
    def get_use_underline(self) -> bool: ...
    def set_title(self, title: str) -> None: ...
    def set_title_selectable(self, title_selectable: bool) -> None: ...
    def set_use_markup(self, use_markup: bool): ...
    def set_use_underline(self, use_underline: bool): ...

class PreferencesWindow:
    def add(self, page: PreferencesPage) -> None: ...
    def add_toast(self, toast: Toast) -> None: ...
    def close_subpage(self) -> None: ...
    def get_can_navigate_back(self) -> bool: ...
    def get_search_enabled(self) -> bool: ...
    def get_visible_page(self) -> Union[PreferencesPage, None]: ...
    def get_visible_page_name(self) -> Union[str, None]: ...
    def present_subpage(self, subpage: Gtk.Widget) -> None: ...
    def remove(self, page: PreferencesPage) -> None: ...
    def set_can_navigate_back(self, can_navigate_back: bool) -> None: ...
    def set_search_enabled(self, search_enabled: bool) -> None: ...
    def set_visible_page(self, page: PreferencesPage) -> None: ...
    def set_visible_page_name(self, name: str) -> None: ...

class PropertyAnimationTarget:
    def get_object(*args, **kwargs): ...
    def get_pspec(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def new_for_pspec(*args, **kwargs): ...

class SplitButton:
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    def get_dropdown_tooltip(*args, **kwargs): ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_label(self) -> Union[str, None]: ...
    def get_menu_model(self) -> Union[Gio.MenuModel, None]: ...
    def get_popover(self) -> Union[Gtk.Popover, None]: ...
    def get_use_underline(self) -> bool: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def popdown(self) -> None: ...
    def popup(self) -> None: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...
    def set_dropdown_tooltip(*args, **kwargs): ...
    def set_icon_name(self, icon_name: str) -> None: ...
    def set_label(self, label: str) -> None: ...
    def set_menu_model(self, menu_model: Union[Gio.MenuModel, None]) -> None: ...
    def set_popover(self, popover: Union[Gtk.Popover, None]) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...

class SpringAnimation:
    def get_clamp(self) -> bool: ...
    def get_epsilon(self) -> float: ...
    def get_estimated_duration(self) -> int: ...
    def get_initial_velocity(self) -> float: ...
    def get_spring_params(self) -> SpringParams: ...
    def get_value_from(self) -> float: ...
    def get_value_to(self) -> float: ...
    def get_velocity(self) -> float: ...
    @classmethod
    def new(
        widget: Gtk.Widget,
        from_: float,
        to: float,
        spring_params: SpringParams,
        target: AnimationTarget,
    ) -> Animation: ...
    def set_clamp(self, clamp: bool) -> None: ...
    def set_epsilon(self, epsilon: float) -> None: ...
    def set_initial_velocity(self, velocity: float) -> None: ...
    def set_spring_params(self, spring_params: SpringParams) -> None: ...
    def set_value_from(self, value: float) -> None: ...
    def set_value_to(self, value: float) -> None: ...

class SpringParams:
    def get_damping(self) -> float: ...
    def get_damping_ratio(self) -> float: ...
    def get_mass(self) -> float: ...
    def get_stiffness(self) -> float: ...
    @classmethod
    def new(damping_ratio: float, mass: float, stiffness: float) -> SpringParams: ...
    @classmethod
    def new_full(damping: float, mass: float, stiffness: float) -> SpringParams: ...
    def ref(self) -> SpringParams: ...
    def unref(self) -> None: ...

class Squeezer:
    def add(self, child: Gtk.Widget) -> None: ...
    def get_allow_none(self) -> bool: ...
    def get_homogeneous(self) -> bool: ...
    def get_interpolate_size(self) -> bool: ...
    def get_page(self, child: Gtk.Widget) -> SqueezerPage: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_switch_threshold_policy(self) -> FoldThresholdPolicy: ...
    def get_transition_duration(self) -> int: ...
    def get_transition_running(self) -> bool: ...
    def get_transition_type(self) -> SqueezerTransitionType: ...
    def get_visible_child(self) -> Union[Gtk.Widget, None]: ...
    def get_xalign(self) -> float: ...
    def get_yalign(self) -> float: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_allow_none(self, allow_none: bool) -> None: ...
    def set_homogeneous(self, homogeneous: bool) -> None: ...
    def set_interpolate_size(self, interpolate_size: bool) -> None: ...
    def set_switch_threshold_policy(self, policy: FoldThresholdPolicy) -> None: ...
    def set_transition_duration(self, duration: int) -> None: ...
    def set_transition_type(self, transition: SqueezerTransitionType) -> None: ...
    def set_xalign(self, xalign: float) -> None: ...
    def set_yalign(self, yalign: float) -> None: ...

class SqueezerPage:
    def get_child(self) -> Gtk.Widget: ...
    def get_enabled(self) -> bool: ...
    def set_enabled(self, enabled: bool) -> None: ...

class StatusPage:
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    def get_description(self) -> Union[str, None]: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_paintable(self) -> Union[Gdk.Paintable, None]: ...
    def get_title(self) -> str: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...
    def set_description(self, description: Union[str, None]) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_paintable(self, paintable: Union[Gdk.Paintable, None]) -> None: ...
    def set_title(self, title: str) -> None: ...

class StyleManager:
    def get_color_scheme(self) -> ColorScheme: ...
    def get_dark(self) -> bool: ...
    @classmethod
    def get_default() -> StyleManager: ...
    def get_display(self) -> Gdk.Display: ...
    @classmethod
    def get_for_display(display: Gdk.Display) -> StyleManager: ...
    def get_high_contrast(self) -> bool: ...
    def get_system_supports_color_schemes(self) -> bool: ...
    def set_color_scheme(self, color_scheme: ColorScheme) -> None: ...

class SwipeTracker:
    def get_allow_long_swipes(self) -> bool: ...
    def get_allow_mouse_drag(self) -> bool: ...
    def get_enabled(self) -> bool: ...
    def get_reversed(self) -> bool: ...
    def get_swipeable(self) -> Swipeable: ...
    @classmethod
    def new(swipeable: Swipeable) -> SwipeTracker: ...
    def set_allow_long_swipes(self, allow_long_swipes: bool) -> None: ...
    def set_allow_mouse_drag(self, allow_mouse_drag: bool) -> None: ...
    def set_enabled(self, enabled: bool) -> None: ...
    def set_reversed(self, reversed: bool) -> None: ...
    def shift_position(self, delta: float) -> None: ...

class Swipeable:
    def get_cancel_progress(self) -> float: ...
    def get_distance(self) -> float: ...
    def get_progress(self) -> float: ...
    def get_snap_points(self) -> list[float]: ...
    def get_swipe_area(
        self, navigation_direction: NavigationDirection, is_drag: bool
    ) -> Gdk.Rectangle: ...

class SwipeableInterface:
    get_cancel_progress = ...
    get_distance = ...
    get_progress = ...
    get_snap_points = ...
    get_swipe_area = ...
    padding = ...
    parent = ...

class TabBar:
    def get_autohide(self) -> bool: ...
    def get_end_action_widget(self) -> Union[Gtk.Widget, None]: ...
    def get_expand_tabs(self) -> bool: ...
    def get_inverted(self) -> bool: ...
    def get_is_overflowing(self) -> bool: ...
    def get_start_action_widget(self) -> Union[Gtk.Widget, None]: ...
    def get_tabs_revealed(self) -> bool: ...
    def get_view(self) -> Union[TabView, None]: ...
    @classmethod
    def new() -> TabBar: ...
    def set_autohide(self, autohide: bool) -> None: ...
    def set_end_action_widget(self, widget: Union[Gtk.Widget, None]) -> None: ...
    def set_expand_tabs(self, expand_tabs: bool) -> None: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_start_action_widget(self, widget: Union[Gtk.Widget, None]) -> None: ...
    def set_view(self, view: Union[TabView, None]) -> None: ...
    def setup_extra_drop_target(
        self, actions: Gdk.DragAction, types: Union[list[GObject.GType], None]
    ) -> None: ...

class TabPage:
    def get_child(self) -> Gtk.Widget: ...
    def get_icon(self) -> Union[Gio.Icon, None]: ...
    def get_indicator_activatable(self) -> bool: ...
    def get_indicator_icon(self) -> Union[Gio.Icon, None]: ...
    def get_indicator_tooltip(*args, **kwargs): ...
    def get_loading(self) -> bool: ...
    def get_needs_attention(self) -> bool: ...
    def get_parent(self) -> Union[TabPage, None]: ...
    def get_pinned(self) -> bool: ...
    def get_selected(self) -> bool: ...
    def get_title(self) -> str: ...
    def get_tooltip(self) -> Union[str, None]: ...
    def set_icon(self, icon: Union[Gio.Icon, None]) -> None: ...
    def set_indicator_activatable(self, activatable: bool) -> None: ...
    def set_indicator_icon(self, indicator_icon: Union[Gio.Icon, None]) -> None: ...
    def set_indicator_tooltip(*args, **kwargs): ...
    def set_loading(self, loading: bool) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_tooltip(self, tooltip: str) -> None: ...

class TabView:
    def add_page(self, child: Gtk.Widget, parent: Union[TabPage, None]) -> TabPage: ...
    def add_shortcuts(*args, **kwargs): ...
    def append(self, child: Gtk.Widget) -> TabPage: ...
    def append_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def close_other_pages(self, page: TabPage) -> None: ...
    def close_page(self, page: TabPage) -> None: ...
    def close_page_finish(self, page: TabPage, confirm: bool) -> None: ...
    def close_pages_after(self, page: TabPage) -> None: ...
    def close_pages_before(self, page: TabPage) -> None: ...
    def get_default_icon(self) -> Gio.Icon: ...
    def get_is_transferring_page(self) -> bool: ...
    def get_menu_model(self) -> Gio.MenuModel: ...
    def get_n_pages(self) -> int: ...
    def get_n_pinned_pages(self) -> int: ...
    def get_nth_page(self, position: int) -> TabPage: ...
    def get_page(self, child: Gtk.Widget) -> TabPage: ...
    def get_page_position(self, page: TabPage) -> int: ...
    def get_pages(self) -> Gtk.SelectionModel: ...
    def get_selected_page(self) -> Union[TabPage, None]: ...
    def get_shortcuts(*args, **kwargs): ...
    def insert(self, child: Gtk.Widget, position: int) -> TabPage: ...
    def insert_pinned(self, child: Gtk.Widget, position: int) -> TabPage: ...
    @classmethod
    def new() -> TabView: ...
    def prepend(self, child: Gtk.Widget) -> TabPage: ...
    def prepend_pinned(self, child: Gtk.Widget) -> TabPage: ...
    def remove_shortcuts(*args, **kwargs): ...
    def reorder_backward(self, page: TabPage) -> bool: ...
    def reorder_first(self, page: TabPage) -> bool: ...
    def reorder_forward(self, page: TabPage) -> bool: ...
    def reorder_last(self, page: TabPage) -> bool: ...
    def reorder_page(self, page: TabPage, position: int) -> bool: ...
    def select_next_page(self) -> bool: ...
    def select_previous_page(self) -> bool: ...
    def set_default_icon(self, default_icon: Gio.Icon) -> None: ...
    def set_menu_model(self, menu_model: Union[Gio.MenuModel, None]) -> None: ...
    def set_page_pinned(self, page: TabPage, pinned: bool) -> None: ...
    def set_selected_page(self, selected_page: TabPage) -> None: ...
    def set_shortcuts(*args, **kwargs): ...
    def transfer_page(
        self, page: TabPage, other_view: TabView, position: int
    ) -> None: ...

class TimedAnimation:
    def get_alternate(self) -> bool: ...
    def get_duration(self) -> int: ...
    def get_easing(self) -> Easing: ...
    def get_repeat_count(self) -> int: ...
    def get_reverse(self) -> bool: ...
    def get_value_from(self) -> float: ...
    def get_value_to(self) -> float: ...
    @classmethod
    def new(
        widget: Gtk.Widget,
        from_: float,
        to: float,
        duration: int,
        target: AnimationTarget,
    ) -> Animation: ...
    def set_alternate(self, alternate: bool) -> None: ...
    def set_duration(self, duration: int) -> None: ...
    def set_easing(self, easing: Easing) -> None: ...
    def set_repeat_count(self, repeat_count: int) -> None: ...
    def set_reverse(self, reverse: bool) -> None: ...
    def set_value_from(self, value: float) -> None: ...
    def set_value_to(self, value: float) -> None: ...

class Toast:
    def dismiss(self) -> None: ...
    def get_action_name(self) -> Union[str, None]: ...
    def get_action_target_value(self) -> Union[GLib.Variant, None]: ...
    def get_button_label(self) -> Union[str, None]: ...
    def get_custom_title(*args, **kwargs): ...
    def get_priority(self) -> ToastPriority: ...
    def get_timeout(self) -> int: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(title: str) -> Toast: ...
    def set_action_name(self, action_name: Union[str, None]) -> None: ...
    def set_action_target_value(
        self, action_target: Union[GLib.Variant, None]
    ) -> None: ...
    def set_button_label(self, button_label: Union[str, None]) -> None: ...
    def set_custom_title(*args, **kwargs): ...
    def set_detailed_action_name(
        self, detailed_action_name: Union[str, None]
    ) -> None: ...
    def set_priority(self, priority: ToastPriority) -> None: ...
    def set_timeout(self, timeout: int) -> None: ...
    def set_title(self, title: str) -> None: ...

class ToastOverlay:
    def add_toast(self, toast: Toast) -> None: ...
    def get_child(self) -> Union[Gtk.Widget, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_child(self, child: Union[Gtk.Widget, None]) -> None: ...

class ViewStack:
    def add(self, child: Gtk.Widget) -> ViewStackPage: ...
    def add_named(self, child: Gtk.Widget, name: Union[str, None]) -> ViewStackPage: ...
    def add_titled(
        self, child: Gtk.Widget, name: Union[str, None], title: str
    ) -> ViewStackPage: ...
    def add_titled_with_icon(*args, **kwargs): ...
    def get_child_by_name(self, name: str) -> Union[Gtk.Widget, None]: ...
    def get_hhomogeneous(self) -> bool: ...
    def get_page(self, child: Gtk.Widget) -> ViewStackPage: ...
    def get_pages(self) -> Gtk.SelectionMode: ...
    def get_vhomogeneous(self) -> bool: ...
    def get_visible_child(self) -> Union[Gtk.Widget, None]: ...
    def get_visible_child_name(self) -> Union[str, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def remove(self, child: Gtk.Widget) -> None: ...
    def set_hhomogeneous(self, hhomogeneous: bool) -> None: ...
    def set_vhomogeneous(self, vhomogeneous: bool) -> None: ...
    def set_visible_child(self, child: Gtk.Widget) -> None: ...
    def set_visible_child_name(self, name: str) -> None: ...

class ViewStackPage:
    def get_badge_number(self) -> int: ...
    def get_child(self) -> Gtk.Widget: ...
    def get_icon_name(self) -> Union[str, None]: ...
    def get_name(self) -> Union[str, None]: ...
    def get_needs_attention(self) -> bool: ...
    def get_title(self) -> Union[str, None]: ...
    def get_use_underline(self) -> bool: ...
    def get_visible(self) -> bool: ...
    def set_badge_number(self, badge_number: int) -> None: ...
    def set_icon_name(self, icon_name: Union[str, None]) -> None: ...
    def set_name(self, name: Union[str, None]) -> None: ...
    def set_needs_attention(self, needs_attention: bool) -> None: ...
    def set_title(self, title: Union[str, None]) -> None: ...
    def set_use_underline(self, use_underline: bool) -> None: ...
    def set_visible(self, visible: bool) -> None: ...

class ViewSwitcher:
    def get_policy(self) -> ViewSwitcherPolicy: ...
    def get_stack(self) -> Union[ViewStack, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_policy(self, policy: ViewSwitcherPolicy) -> None: ...
    def set_stack(self, stack: Union[ViewStack, None]) -> None: ...

class ViewSwitcherBar:
    def get_reveal(self) -> bool: ...
    def get_stack(self) -> Union[ViewStack, None]: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_reveal(self, reveal: bool) -> None: ...
    def set_stack(self, stack: Union[ViewStack, None]) -> None: ...

class ViewSwitcherTitle:
    def get_stack(self) -> Union[ViewStack, None]: ...
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    def get_title_visible(self) -> bool: ...
    def get_view_switcher_enabled(self) -> bool: ...
    @classmethod
    def new() -> Gtk.Widget: ...
    def set_stack(self, stack: Union[ViewStack, None]) -> None: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_view_switcher_enabled(self, enabled: bool) -> None: ...

class Window:
    def get_content(self) -> Union[Gtk.Widget, None]: ...
    def set_content(self, content: Union[Gtk.Widget, None]) -> None: ...

class WindowTitle:
    def get_subtitle(self) -> str: ...
    def get_title(self) -> str: ...
    @classmethod
    def new(title: str, subtitle: str) -> Gtk.Widget: ...
    def set_subtitle(self, subtitle: str) -> None: ...
    def set_title(self, title: str) -> None: ...

class TabViewShortcuts(GObject.GFlags):
    ALL_SHORTCUTS = ...
    ALT_DIGITS = ...
    ALT_ZERO = ...
    CONTROL_END = ...
    CONTROL_HOME = ...
    CONTROL_PAGE_DOWN = ...
    CONTROL_PAGE_UP = ...
    CONTROL_SHIFT_END = ...
    CONTROL_SHIFT_HOME = ...
    CONTROL_SHIFT_PAGE_DOWN = ...
    CONTROL_SHIFT_PAGE_UP = ...
    CONTROL_SHIFT_TAB = ...
    CONTROL_TAB = ...
    NONE = ...

class AnimationState(GObject.GEnum):
    FINISHED = ...
    IDLE = ...
    PAUSED = ...
    PLAYING = ...

class CenteringPolicy(GObject.GEnum):
    LOOSE = ...
    STRICT = ...

class ColorScheme(GObject.GEnum):
    DEFAULT = ...
    FORCE_DARK = ...
    FORCE_LIGHT = ...
    PREFER_DARK = ...
    PREFER_LIGHT = ...

class Easing(GObject.GEnum):
    EASE_IN_BACK = ...
    EASE_IN_BOUNCE = ...
    EASE_IN_CIRC = ...
    EASE_IN_CUBIC = ...
    EASE_IN_ELASTIC = ...
    EASE_IN_EXPO = ...
    EASE_IN_OUT_BACK = ...
    EASE_IN_OUT_BOUNCE = ...
    EASE_IN_OUT_CIRC = ...
    EASE_IN_OUT_CUBIC = ...
    EASE_IN_OUT_ELASTIC = ...
    EASE_IN_OUT_EXPO = ...
    EASE_IN_OUT_QUAD = ...
    EASE_IN_OUT_QUART = ...
    EASE_IN_OUT_QUINT = ...
    EASE_IN_OUT_SINE = ...
    EASE_IN_QUAD = ...
    EASE_IN_QUART = ...
    EASE_IN_QUINT = ...
    EASE_IN_SINE = ...
    EASE_OUT_BACK = ...
    EASE_OUT_BOUNCE = ...
    EASE_OUT_CIRC = ...
    EASE_OUT_CUBIC = ...
    EASE_OUT_ELASTIC = ...
    EASE_OUT_EXPO = ...
    EASE_OUT_QUAD = ...
    EASE_OUT_QUART = ...
    EASE_OUT_QUINT = ...
    EASE_OUT_SINE = ...
    LINEAR = ...
    ease = ...

class FlapFoldPolicy(GObject.GEnum):
    ALWAYS = ...
    AUTO = ...
    NEVER = ...

class FlapTransitionType(GObject.GEnum):
    OVER = ...
    SLIDE = ...
    UNDER = ...

class FoldThresholdPolicy(GObject.GEnum):
    MINIMUM = ...
    NATURAL = ...

class LeafletTransitionType(GObject.GEnum):
    OVER = ...
    SLIDE = ...
    UNDER = ...

class NavigationDirection(GObject.GEnum):
    BACK = ...
    FORWARD = ...

class ResponseAppearance(GObject.GEnum):
    DEFAULT = ...
    DESTRUCTIVE = ...
    SUGGESTED = ...

class SqueezerTransitionType(GObject.GEnum):
    CROSSFADE = ...
    NONE = ...

class ToastPriority(GObject.GEnum):
    HIGH = ...
    NORMAL = ...

class ViewSwitcherPolicy(GObject.GEnum):
    NARROW = ...
    WIDE = ...