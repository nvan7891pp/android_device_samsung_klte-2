# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Custom OTA commands for hlte devices"""

def FullOTA_InstallEnd(info):
  info.script.AppendExtra('ifelse(is_substring("G900T", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp /system/lib/gsm/* /system/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("G9005", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp /system/lib/gsm/* /system/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("G900W", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp /system/lib/gsm/* /system/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("G900V", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp /system/lib/cdma/* /system/lib/"));')
  info.script.AppendExtra('ifelse(is_substring("G900P", getprop("ro.bootloader")), run_program("/sbin/sh", "-c", "busybox cp /system/lib/cdma/* /system/lib/"));')
  info.script.AppendExtra('delete_recursive("/system/lib/gsm/");')
  info.script.AppendExtra('delete_recursive("/system/lib/cdma/");')
