# Embedded file name: C:\ProgramData\Ableton\Live 9 Beta\Resources\MIDI Remote Scripts\LPC_Live_2\LPCM4LInterfaceMixin.py


class Launchpad95M4LInterfaceMixin(object):
    """ LPCM4LInterfaceMixin is a mixin to be used with MainSelectorComponent that provides a listenable property for M4L and refresh functions for classes. """

    def init_m4l_interface(self):
        """ Initializes the interface. """
        self._refresh_type = 'map'
        self._refresh_listener = None
        return

    def disconnect_m4l_interface(self):
        """ Disconnects the interface. """
        self._refresh_listener = None
        return

    @property
    def refresh(self):
        """ Returns the type of refresh to perform. """
        return self._refresh_type

    def add_refresh_listener(self, listener):
        """ Adds a refresh listener.  This only allows one listener to be added. """
        self._refresh_listener = listener

    def remove_refresh_listener(self, listener):
        """ Removes the refresh listener. """
        self._refresh_listener = None
        return

    def refresh_has_listener(self, listener):
        """ Returns whether refresh has a listener. """
        return self._refresh_listener is not None

    def refresh_map_display(self, args = None):
        """ Refreshes the M4L device's map display. """
        self._refresh_type = 'map'
        self._notify_listener()

    def refresh_status_display(self, args = None):
        """ Refreshes the M4L device's entire status display. """
        self._refresh_type = 'status'
        self._notify_listener()

    def refresh_attributes(self, args = None):
        """ Refreshes the M4L device's attribute display. """
        self._refresh_type = 'attributes'
        self._notify_listener()

    def refresh_info(self, args = None):
        """ Refreshes the M4L device's info display. """
        self._refresh_type = 'info'
        self._notify_listener()

    def toggle_status(self, args = None):
        """ Toggles the status display on/off. """
        self._refresh_type = 'status_toggle'
        self._notify_listener()

    def toggle_map(self, args = None):
        """ Toggles the map display on/off. """
        self._refresh_type = 'map_toggle'
        self._notify_listener()

    def _notify_listener(self):
        """ Notifies listener (M4L device) that a refresh is needed. """
        if self._refresh_listener is not None:
            self._refresh_listener()
        return