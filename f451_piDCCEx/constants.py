"""Global constants for f451 Labs piRED & piDCCEx applications

This module holds all global constants used within the components of the 
f451 Labs piRED and piDCCEx applications. Some of the constants are used 
as keyword equivalents for attributes listed in the `settings.toml` file.
"""

# fmt: off
# =========================================================
#              M I S C .   C O N S T A N T S
# =========================================================
DEF_FREQ = 600                  # Default delay between uploads in seconds
DEF_DELAY = 300                 # Default delay before first upload in seconds
DEF_WAIT = 1                    # Default delay between sensor reads
DEF_THROTTLE = 120              # Default additional delay on 'ThrottlingError'
DEF_ROUNDING = 2                # Default 'rounding' precision for uploaded data
# fmt: on


# =========================================================
#    K E Y W O R D S   F O R   C O N F I G   F I L E S
# =========================================================
KWD_FREQ = 'FREQ'
KWD_DELAY = 'DELAY'
KWD_WAIT = 'WAIT'
KWD_THROTTLE = 'THROTTLE'
KWD_ROUNDING = 'ROUNDING'

# -- Support for internet speed data --
KWD_FEED_DWNLD = 'FEED_DWNLD'
KWD_FEED_UPLD = 'FEED_UPLD'
KWD_FEED_PING = 'FEED_PING'

KWD_DATA_DWNLD = 'download'
KWD_DATA_UPLD = 'upload'
KWD_DATA_PING = 'ping'

# fmt: off
# =========================================================
#   C O N S T A N T S   F O R   D I S P L A Y   M O D E S
# =========================================================
DISPL_DWNLD = KWD_DATA_DWNLD    # Display download speed
DISPL_UPLD = KWD_DATA_UPLD      # Display upload speed
DISPL_PING = KWD_DATA_PING      # Display ping response time

# -- SpeedTest --
MBITS_PER_SEC = 1048576         # 1 MB = 1024 * 1024
MAX_SPEED_MB = 3000             # Max Download speed = 3 Gbps = 3,000 Mbps
# fmt: on
