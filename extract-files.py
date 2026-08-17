#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 Paranoid Android
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import blob_fixup, blob_fixups_user_type
from extract_utils.main import ExtractUtils
from extract_utils_gms.module import ExtractUtilsGmsModule


blob_fixups: blob_fixups_user_type = {
    (
        'product/apex/com.google.android.gmssystem.prodvic.apex',
        'product/app/Gmail2/Gmail2.apk',
        'product/app/Maps/Maps.apk',
        'product/app/Photos/Photos.apk',
        'product/app/TrichromeLibrary64/TrichromeLibrary64.apk',
        'product/app/WebViewGoogle64/WebViewGoogle64.apk',
        'product/app/YouTube/YouTube.apk',
        'product/priv-app/GmsCore/GmsCore.apk',
        'product/priv-app/Messages/Messages.apk',
        'product/priv-app/Phonesky/Phonesky.apk',
        'product/priv-app/Velvet/Velvet.apk',
    ): blob_fixup().split_file_parts('99M'),
}  # fmt: skip


module = ExtractUtilsGmsModule(
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
