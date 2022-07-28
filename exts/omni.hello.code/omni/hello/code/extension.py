import omni.ext
import omni.ui as ui

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.hello.code] MyExtension startup")

        self._window_example = ui.Window("My", width=300, height=300)
        with self._window_example.frame:
            with ui.VStack(height=0):
                ui.Label("Some Label")

                def on_click():
                    print("clicked!")

                def size_me(window):
                    window.width = 300
                    window.height = 300

                ui.Button("Click Me", clicked_fn=lambda: on_click())
                ui.Button("Moveto (200, 200)", clicked_fn=lambda w=self._window_example: size_me(w))

    def on_shutdown(self):
        print("[omni.hello.code] MyExtension shutdown")