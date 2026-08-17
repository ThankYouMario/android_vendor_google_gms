#
# SPDX-FileCopyrightText: 2026 Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from os import path
from typing import Optional

from extract_utils.fixups_blob import blob_fixups_user_type
from extract_utils.module import ExtractUtilsModule
from extract_utils.utils import remove_dir_contents

class ExtractUtilsGmsModule(ExtractUtilsModule):
    def __init__(
        self,
        blob_fixups: Optional[blob_fixups_user_type] = None,
    ):
        super().__init__(
            device='gms',
            vendor='google',
            device_rel_path=path.join('vendor', 'google', 'gms'),
            blob_fixups=blob_fixups,
        )

    def cleanup(self):
        for proprietary_file in self.proprietary_files:
            vendor_path = self.proprietary_file_vendor_path(proprietary_file)
            remove_dir_contents(vendor_path)
