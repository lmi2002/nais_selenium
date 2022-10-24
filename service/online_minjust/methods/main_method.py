import os
import time

from helpers.func import get_list_files
from settings.setting_browser import SettingsBrowser


class OnlineMinjustMainMethod:
    dirname = SettingsBrowser().get_download_dir_pdf()

    def get_list_download_files(self):
        return (set(get_list_files(self.dirname)))

    def update_list_download_files(self, qty):
        timeout = 60
        poll = 0.5
        end_time = time.time() + timeout
        while True:
            qty_new = len(self.get_list_download_files())
            if qty_new > qty and "download" in qty_new:
                return True
            time.sleep(poll)
            if time.time() > end_time:
                break
        raise ('Not found download new pdf')

    def get_abspath_file(self, name_file):
        return os.path.join(self.dirname, name_file)

    def get_first_file(self, set_files):
        for elem in set_files:
            if elem.endswith('.crdownload'):
                elem.replace('.crdownload', '')
            return elem
