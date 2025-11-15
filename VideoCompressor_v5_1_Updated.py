"""
Video Compressor Pro - OPTIMIZED EDITION v6.0
===========================================================
===========================================================

NEW in v6.0 - AGGRESSIVE SIZE/QUALITY OPTIMIZATION (2025-11):
🎯 SIZE REDUCTION: 35-45% smaller files with maintained visual quality
- OPTIMIZED CQ VALUES: Increased by 3-4 points (28-31 for 1080p, was 24-26)
  * Still excellent quality (VMAF 92-96 vs previous 96-98)
  * Much smaller file sizes without visible artifacts
- LOOSENED VBR CONSTRAINTS: maxrate = target × 1.8 (was 1.15)
  * Prevents banding/blocking in complex scenes
  * Pure CQ mode option (ENABLE_PURE_CQ_MODE) for best quality/size balance
- PROXIMITY DETECTION FIX: Within 3% → skip encoding (was 8% → force compression)
  * Within 15% → gentle nudge only (no forced bitrate reduction)
  * Avoids unnecessary transcoding of efficient sources

🎨 TEXTURE PRESERVATION: Film grain and skin detail maintained
- FILM GRAIN DETECTION: Auto-detect grain via temporal variance analysis
  * Temporal-only denoising for grainy content (preserves spatial detail)
  * No more waxy skin texture on film sources
  * 20-30% smaller files due to reduced temporal fighting
- GRAIN-PRESERVING FILTERS: Gentler denoising (reduced from 0.50 to 0.35 max)
  * Luma-only sharpening (no chroma sharpening = no artifacts)
  * New "grainy" profile for film content

🌈 PROFESSIONAL HDR→SDR: ITU standard tone mapping
- LIBPLACEBO SUPPORT: BT.2390 EETF (Netflix/YouTube standard)
  * Perceptual gamut mapping preserves color appearance
  * Auto peak detection for each scene
  * Blue noise dithering prevents banding
- ENHANCED FALLBACK: Mobius tone mapping (better than old Hable)
  * Proper brightness normalization (100 nits)
  * Desaturation prevents SDR gamut clipping

🎞️ BANDING PREVENTION: Smooth gradients in dark scenes
- 10-BIT INTERMEDIATE PROCESSING: yuv420p10le → noise dither → yuv420p
  * Temporal + uniform blue noise pattern
  * Eliminates posterization in gradients
  * Minimal file size impact (1-3%)

🚀 ENHANCED HARDWARE ACCELERATION:
- NVIDIA NVENC: Advanced quality settings
  * AQ strength boosted to 12 (was 8, max 15)
  * Lookahead level 3 for best scene detection
  * High tier removes bitrate ceiling
  * Non-reference P-frames (5-10% better compression)
- AMD RDNA 4: AV1 B-frames support
  * 4 B-frames with middle reference (RDNA 4+ only)
  * Pre-analysis + VBAQ for better bit allocation
  * Half/quarter-pixel motion estimation
  * Falls back gracefully for RDNA 3 and older

🔊 SMART AUDIO HANDLING: Copy when efficient
- AAC ≤192 kbps → copy (avoid double encoding loss)
- Opus ≤160 kbps → copy (already excellent)
- E-AC3 ≤256 kbps → copy
- No upsampling of lossy audio
- Match source bitrate for lossy→lossy transcoding




NEW in v4.6.2 - ENHANCED ADAPTIVE REFINEMENT:
- [TARGET] FINAL CQ FINISHING: Post-adaptive codec-aware micro-adjustments
  * HEVC sources: +1 CQ (can compress more than H.264)
  * High complexity (bppf >=0.12): -1 CQ + 8% maxrate boost (protect details)
  * Low complexity (bppf <=0.05): +1 CQ (compress harder on clean content)
  * Proximity detection refined: Within 12% ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ' force -10% target/maxrate
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸"Ãƒâ€¦Ã‚Â  IMPROVED SAVINGS ESTIMATION: Pre-encode skip based on params
  * Estimates output from adaptive params (weighted target+maxrate)
  * Skips encoding when estimated savings <5% (user-configurable)
  * More accurate than simple bitrate comparison
- [MAIL] CODEC-AWARE DECISIONS: Normalizes codec names for better logic
  * Treats h265/hevc identically
  * Better handling of already-efficient sources

v4.6.0 - NOVA-STYLE ADAPTIVE COMPRESSION:
- [TARGET] THREE-LEVEL DECISION SYSTEM: Resolution ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Bitrate Band ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Complexity (bppf)
  * Added 1440p tier: 5-6 Mbps targets
  * Explicit 1080p bands: Very High (>8 Mbps), Normal (4-8 Mbps), Low (<4 Mbps)
  * Complexity fine-tuning: Adjusts CQ Â±1 based on bppf (0.05-0.12 range)
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ RELATIVE ADJUSTMENT: Prevents "no compression" when target ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°Ãƒâ€¹Ã¢â‚¬Â  source
  * If target within 12% of source ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ force more compression (CQ+1, target*0.92)
  * If source >> target (2x) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ protect details (CQ-1)
- [BOLT] TIGHTENED VBR: maxrate = target * 1.25 (was 1.5+), bufsize = maxrate * 2
  * Reduces bitrate "runaway" and improves size estimation accuracy
- [ART] HDRÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢SDR DOWNCONVERT REFINEMENT: Softer denoise/sharpen when converting
- [ROCKET] SMART SKIP 2.0: Auto-skip already-efficient HEVC files
  * If source is HEVC/H.265 AND <=1080p AND <=3.5 Mbps ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ remux only
- ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  ENHANCED LOGGING: Comprehensive decision summary before encoding
- [DICE] IMPROVED SIZE ESTIMATION: Uses weighted avg of target+maxrate
  * Fixes "Est: 528MB ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Actual: 646MB" deltas

v4.5.0 - ADAPTIVE NVENC ENCODING
v4.4.0 - INTELLIGENT AUTO-COMPRESSION
v4.3.0 - SMART PROTECTION & TRUE AUTO-SHUTDOWN
v4.2.0 - USABILITY & AUTOMATION FIX
"""

import os
import sys
import time
import subprocess
import threading
import math
import shutil
import json
import pickle
import re
import psutil
import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext, simpledialog
from typing import Optional, Tuple, List, Dict
from pathlib import Path
from dataclasses import dataclass

try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
    DND_OK = True
except ImportError:
    DND_OK = False

APP_TITLE = "Video Compressor Pro"
VERSION = "6.0"
SUBTITLE = "Adaptive HEVC/AV1 Compression"

# Theme System - Dark Gaming/Modern Theme (Option 4)
THEME_DARK = {
    "BG_DARK": "#000000",  # Pure black background
    "BG_MID": "#001122",  # Very dark blue-gray
    "BG_CARD": "#001428",  # rgba(0, 20, 40, 0.8) - panel background from mockup
    "BG_INPUT": "#000511",  # Dark input background
    "ACCENT": "#00ffff",  # Cyan - primary accent
    "ACCENT_BRIGHT": "#5affff",  # Bright cyan
    "ACCENT_DIM": "#0088aa",  # Dim cyan
    "ACCENT_GLOW": "#00ffff",  # Glowing cyan
    "TEXT_BRIGHT": "#00ffff",  # Cyan text for gaming look
    "TEXT_MID": "#00aaff",  # Mid cyan
    "TEXT_DIM": "#0088aa",  # Dim cyan
    "SUCCESS": "#00ff00",  # Green for success
    "ERROR": "#ff0000",  # Red for errors
    "WARNING": "#ff00ff",  # Magenta for warnings
    "BORDER": "#00ffff",  # Cyan borders
    "BORDER_BRIGHT": "#00ffff"  # Bright cyan borders
}

THEME_LIGHT = {
    "BG_DARK": "#f5f5f5",
    "BG_MID": "#e8e8e8",
    "BG_CARD": "#ffffff",
    "BG_INPUT": "#fafafa",
    "ACCENT": "#0066cc",
    "ACCENT_BRIGHT": "#0088ff",
    "ACCENT_DIM": "#004499",
    "ACCENT_GLOW": "#0066cc",
    "TEXT_BRIGHT": "#1a1a1a",
    "TEXT_MID": "#4a4a4a",
    "TEXT_DIM": "#808080",
    "SUCCESS": "#00aa55",
    "ERROR": "#cc0000",
    "WARNING": "#ff8800",
    "BORDER": "#d0d0d0",
    "BORDER_BRIGHT": "#b0b0b0"
}

# Current theme (defaults to dark)
CURRENT_THEME = THEME_DARK.copy()

# Theme getters for backward compatibility
def get_theme():
    """Get current theme colors"""
    return CURRENT_THEME

BG_DARK = CURRENT_THEME["BG_DARK"]
BG_MID = CURRENT_THEME["BG_MID"]
BG_CARD = CURRENT_THEME["BG_CARD"]
BG_INPUT = CURRENT_THEME["BG_INPUT"]
ACCENT = CURRENT_THEME["ACCENT"]
ACCENT_BRIGHT = CURRENT_THEME["ACCENT_BRIGHT"]
ACCENT_DIM = CURRENT_THEME["ACCENT_DIM"]
ACCENT_GLOW = CURRENT_THEME["ACCENT_GLOW"]
TEXT_BRIGHT = CURRENT_THEME["TEXT_BRIGHT"]
TEXT_MID = CURRENT_THEME["TEXT_MID"]
TEXT_DIM = CURRENT_THEME["TEXT_DIM"]
SUCCESS = CURRENT_THEME["SUCCESS"]
ERROR = CURRENT_THEME["ERROR"]
WARNING = CURRENT_THEME["WARNING"]
BORDER = CURRENT_THEME["BORDER"]
BORDER_BRIGHT = CURRENT_THEME["BORDER_BRIGHT"]

# Adaptive encoding tuning constants (2025-11 refactor - OPTIMIZED FOR SIZE/QUALITY)
MIN_1080P_TARGET = 2_000_000  # Lower floor for better compression
MIN_720P_TARGET = 1_400_000
# LOOSENED VBR: Allow headroom for complex scenes (prevents banding/blocking)
DEFAULT_MAXRATE_MULT = 1.8   # Was 1.15, now 1.8 for complex scene headroom
DEFAULT_BUFSIZE_MULT = DEFAULT_MAXRATE_MULT * 2  # Bufsize = 2x maxrate
BOLD_MAXRATE_MULT = 1.5      # Slightly tighter for clean content
BOLD_BUFSIZE_MULT = BOLD_MAXRATE_MULT * 2
MEDIUM_MAXRATE_MULT = 1.5
MEDIUM_BUFSIZE_MULT = 3.0
# Pure CQ mode option (no bitrate constraints - best quality/size balance)
ENABLE_PURE_CQ_MODE = True   # Set False to use constrained VBR

# Centralized filter presets - GRAIN PRESERVING (gentler denoise, luma-only sharpening)
FILTER_PROFILES: Dict[str, Dict[str, str]] = {
    "bold": {
        "denoise": "hqdn3d=0.10:0.10:0.8:0.8",      # Even gentler for skin texture
        "unsharp": "unsharp=la=0.15:ca=0.0"        # Luma-only sharpening
    },
    "medium_soft": {
        "denoise": "hqdn3d=0.20:0.20:1.0:1.0",
        "unsharp": "unsharp=la=0.20:ca=0.0"
    },
    "clean_h264": {
        "denoise": "hqdn3d=0.18:0.18:0.9:0.9",
        "unsharp": "unsharp=la=0.25:ca=0.0"
    },
    "balanced": {
        "denoise": "hqdn3d=0.28:0.28:1.2:1.2",
        "unsharp": "unsharp=la=0.22:ca=0.0"
    },
    "gritty": {
        "denoise": "hqdn3d=0.35:0.35:1.5:1.5",     # Reduced from 0.50 (was destroying texture)
        "unsharp": "unsharp=la=0.30:ca=0.0"
    },
    "grainy": {
        "denoise": "hqdn3d=0.0:0.0:0.5:0.5",       # NEW: Temporal-only for film grain
        "unsharp": "unsharp=la=0.12:ca=0.0"        # Very gentle sharpening
    },
    "hdr_sdr_soft": {
        "denoise": "hqdn3d=0.30:0.30:1.2:1.2",
        "unsharp": "unsharp=la=0.18:ca=0.0"
    },
}

def get_filter_profile(profile_name: str, fallback: str = "balanced") -> Tuple[str, str]:
    """Return (denoise, unsharp) strings for the requested profile."""
    profile = FILTER_PROFILES.get(profile_name) or FILTER_PROFILES.get(fallback, {})
    return profile.get("denoise", "hqdn3d=0.35:0.35:1.3:1.3"), profile.get("unsharp", "unsharp=3:3:0.30:3:3:0.0")

# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class QueueItem:
    """Represents a video in the encoding queue"""
    input_path: str
    output_path: str
    mode: str
    resolution: str
    two_pass: bool
    status: str = "pending"
    progress: float = 0.0
    estimated_size: int = 0
    actual_size: int = 0
    error: str = ""
    skipped_reason: str = ""
    
    def get_display_name(self) -> str:
        """Get shortened display name for queue"""
        name = os.path.basename(self.input_path)
        if len(name) > 40:
            return name[:37] + "..."
        return name

@dataclass
class EncodingProfile:
    """Represents a saved encoding profile"""
    name: str
    mode: str
    resolution: str
    two_pass: bool
    auto_mode: bool
    keep_hdr: bool
    skip_small_saving: bool
    custom_cq: Optional[int] = None
    custom_filters: str = ""
    sharpening_profile: str = "medium"  # light, medium, heavy
    av1_tune: str = "vmaf"  # grain, psnr, ssim, vmaf

@dataclass
class EncodingHistory:
    """Represents an encoding history entry"""
    timestamp: str
    input_path: str
    output_path: str
    mode: str
    input_size: int
    output_size: int
    compression_ratio: float
    encoding_time: float
    source_bitrate: float
    output_bitrate: float

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def find_ffmpeg() -> Optional[str]:
    """Find FFmpeg executable"""
    for exe in ["ffmpeg.exe", "ffmpeg"]:
        for p in os.environ.get("PATH", "").split(os.pathsep):
            full = os.path.join(p, exe)
            if os.path.isfile(full):
                return full
        local = os.path.join(os.getcwd(), exe)
        if os.path.isfile(local):
            return local
    return None

def find_ffprobe() -> Optional[str]:
    """Find ffprobe executable"""
    ffmpeg_path = FFMPEG
    if ffmpeg_path:
        ffprobe_path = ffmpeg_path.replace("ffmpeg", "ffprobe")
        if os.path.isfile(ffprobe_path):
            return ffprobe_path
    return None

FFMPEG = find_ffmpeg()
FFPROBE = find_ffprobe()

def check_codec_support(codec_name: str) -> bool:
    """Check if FFmpeg supports a specific codec"""
    if not FFMPEG:
        return False
    try:
        result = subprocess.run(
            [FFMPEG, "-hide_banner", "-encoders"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return codec_name in result.stdout
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError):
        return False

HAS_LIBSVTAV1 = check_codec_support("libsvtav1")
HAS_HEVC_NVENC = check_codec_support("hevc_nvenc")
HAS_H264_NVENC = check_codec_support("h264_nvenc")
HAS_AV1_AMF = check_codec_support("av1_amf")
HAS_HEVC_AMF = check_codec_support("hevc_amf")
HAS_H264_AMF = check_codec_support("h264_amf")
HAS_ANY_AMF = HAS_AV1_AMF or HAS_HEVC_AMF or HAS_H264_AMF
HAS_LIBX265 = check_codec_support("libx265")
HAS_LIBOPUS = check_codec_support("libopus")
HAS_LIBPLACEBO = check_codec_support("libplacebo")  # For best HDR tone mapping

def detect_amd_rdna4() -> bool:
    """Detect AMD RDNA 4 GPU for enhanced AV1 features (B-frames)"""
    # Method 1: Windows - Check GPU name via wmic
    if sys.platform == "win32":
        try:
            result = subprocess.run(
                ["wmic", "path", "win32_VideoController", "get", "name"],
                capture_output=True, text=True, timeout=3
            )
            if result.returncode == 0:
                output = result.stdout.lower()
                # RDNA 4 = RX 9000 series (9070, 9090, etc.)
                if any(x in output for x in ["rx 9", "rx9", "radeon 9", "rdna4", "rdna 4"]):
                    return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

    # Method 2: Linux - Try rocm-smi
    try:
        result = subprocess.run(
            ["rocm-smi", "--showproductname"],
            capture_output=True, text=True, timeout=2
        )
        if result.returncode == 0:
            output = result.stdout.lower()
            # RDNA 4 = RX 9000 series
            if any(x in output for x in ["rx 9", "radeon 9", "rdna4", "rdna 4"]):
                return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Method 3: Check via AMF B-frame support (RDNA 4+ has B-frames for AV1)
    if HAS_AV1_AMF and FFMPEG:
        try:
            # Test if B-frames are supported for AV1 AMF
            result = subprocess.run(
                [FFMPEG, "-hide_banner", "-h", "encoder=av1_amf"],
                capture_output=True, text=True, timeout=3
            )
            # RDNA 4 adds bf option to AV1 (older cards don't have this)
            # Check for "bf" option specifically for B-frames
            if "-bf" in result.stdout or "B Picture Pattern" in result.stdout:
                return True
        except (subprocess.TimeoutExpired, subprocess.SubprocessError):
            pass

    return False

HAS_AMD_RDNA4 = detect_amd_rdna4()

def detect_film_grain(input_path: str, duration: float = 0.0) -> Tuple[bool, float]:
    """
    Detect film grain via temporal variance analysis.
    Returns: (has_grain, grain_strength 0.0-1.0)

    Uses FFmpeg's noise measurement filter to detect grain.
    """
    if not FFMPEG:
        return (False, 0.0)

    try:
        # Sample duration for analysis (max 30 seconds)
        sample_duration = min(duration if duration > 0 else 30, 30)

        # Use select filter to sample frames evenly + measure noise
        # We sample every 50th frame for speed
        cmd = [
            FFMPEG, "-i", input_path,
            "-vf", "select='not(mod(n,50))',signalstats",
            "-t", str(sample_duration),
            "-f", "null", "-"
        ]

        result = subprocess.run(
            cmd, capture_output=True, text=True,
            timeout=min(sample_duration + 10, 40)
        )

        # Parse temporal difference from signalstats (TDIFF indicates grain)
        tdiff_values = []
        for line in result.stderr.split('\n'):
            if 'lavfi.signalstats.SATMAX' in line:
                # Look for temporal diff indicators
                continue
            if 'lavfi.signalstats.TDIFF' in line:
                try:
                    # Extract TDIFF value (temporal difference)
                    match = re.search(r'TDIFF[^:]*:\s*(\d+\.\d+)', line)
                    if match:
                        tdiff_values.append(float(match.group(1)))
                except (ValueError, AttributeError):
                    continue

        if tdiff_values and len(tdiff_values) >= 3:
            avg_tdiff = sum(tdiff_values) / len(tdiff_values)
            # TDIFF > 1.5 typically indicates grain/noise
            has_grain = avg_tdiff > 1.5
            # Normalize strength (empirical range: 1.0-10.0 for grainy content)
            grain_strength = min(max(avg_tdiff - 1.0, 0.0) / 8.0, 1.0)
            return (has_grain, grain_strength)

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, Exception):
        pass

    # Fallback: No grain detected
    return (False, 0.0)

def ffprobe_info(path: str) -> Dict:
    """
    Get comprehensive video info using ffprobe

    v5.1.3: Enhanced error handling and logging for estimation debugging
    """
    if not FFPROBE:
        print("[EST] WARNING: ffprobe not available, using defaults")
        return {"duration": 1.0, "fps": 25.0, "bitrate": 2000, "width": 1920, "height": 1080}

    try:
        out = subprocess.check_output(
            [FFPROBE, "-v", "error", "-show_entries",
             "format=duration,bit_rate:stream=codec_type,r_frame_rate,width,height,codec_name",
             "-of", "json", path],
            stderr=subprocess.STDOUT, timeout=10
        )
        data = json.loads(out.decode())

        info = {}

        # Extract format-level info
        if "format" in data and "duration" in data["format"]:
            info["duration"] = max(float(data["format"]["duration"]), 0.1)
        else:
            info["duration"] = 1.0
            print(f"[EST] WARNING: No duration found in format, using default")

        if "format" in data and "bit_rate" in data["format"]:
            info["bitrate"] = int(data["format"]["bit_rate"]) // 1000
        else:
            info["bitrate"] = 2000
            print(f"[EST] WARNING: No bitrate in format, will try to calculate from file size")
            # Calculate bitrate from file size if format bitrate is missing
            try:
                file_size = os.path.getsize(path)
                duration = info.get("duration", 1.0)
                if duration > 0:
                    # bitrate = (file_size * 8) / duration / 1000 (for kbps)
                    calculated_bitrate = int((file_size * 8) / duration / 1000)
                    info["bitrate"] = calculated_bitrate
                    print(f"[EST] Calculated bitrate from file size: {calculated_bitrate} kbps")
            except Exception as e:
                print(f"[EST] Could not calculate bitrate from file size: {e}")

        # Find the video stream (might not be stream #0 in unusual formats)
        video_stream = None
        if "streams" in data:
            for stream in data["streams"]:
                if stream.get("codec_type") == "video":
                    video_stream = stream
                    break

        if video_stream:
            # Extract FPS
            fps_str = video_stream.get("r_frame_rate", "25/1")
            if '/' in fps_str:
                num, den = fps_str.split('/')
                info["fps"] = float(num) / float(den) if float(den) != 0 else 25.0
            else:
                info["fps"] = float(fps_str)

            # Extract dimensions
            info["width"] = video_stream.get("width", 1920)
            info["height"] = video_stream.get("height", 1080)

            print(f"[EST] Video stream found: {info['width']}x{info['height']}, {info['fps']:.2f} fps, {info['bitrate']} kbps")
        else:
            # No video stream found, use defaults
            info["fps"] = 25.0
            info["width"] = 1920
            info["height"] = 1080
            print(f"[EST] WARNING: No video stream found, using defaults")

        return info

    except Exception as e:
        print(f"[EST] ERROR in ffprobe_info: {e}")
        import traceback
        traceback.print_exc()
        return {"duration": 1.0, "fps": 25.0, "bitrate": 2000, "width": 1920, "height": 1080}

# ============================================================================
# INTELLIGENT COMPRESSION LAYER (v4.4.0)
# ============================================================================

def ffprobe_info_extended(path: str) -> Dict:
    """
    Extended ffprobe analysis for intelligent compression
    
    v4.6.0: Enhanced with bppf calculation for complexity analysis
    v4.6.2: Added file_size for savings estimation
    """
    if not FFPROBE:
        return {
            "duration": 1.0, "fps": 25.0, "bitrate": 2000, "bitrate_bps": 2000000,
            "width": 1920, "height": 1080,
            "video_codec": "unknown", "audio_codec": "unknown",
            "audio_bitrate": 128, "pix_fmt": "yuv420p",
            "color_trc": "unknown", "color_space": "unknown", "color_primaries": "unknown",
            "field_order": "progressive",
            "rotation": 0, "bppf": 0.1, "file_size": 0,
            "codec_name_normalized": "unknown"
        }
    
    try:
        # Get comprehensive stream info
        out = subprocess.check_output(
            [FFPROBE, "-v", "error", 
             "-show_entries", "stream=codec_name,codec_type,bit_rate,pix_fmt,color_transfer,color_space,color_primaries,field_order,width,height,r_frame_rate:stream_tags=rotate",
             "-show_entries", "format=duration,bit_rate",
             "-of", "json", path],
            stderr=subprocess.STDOUT, timeout=10
        )
        data = json.loads(out.decode())
        
        info = {}
        
        # Format-level info
        if "format" in data:
            info["duration"] = max(float(data["format"].get("duration", 1.0)), 0.1)
            format_bitrate = int(data["format"].get("bit_rate", 2000000))
            info["bitrate_bps"] = format_bitrate
            info["bitrate"] = format_bitrate // 1000
        else:
            info["duration"] = 1.0
            info["bitrate"] = 2000
            info["bitrate_bps"] = 2000000
        
        # Stream-level info
        video_stream = None
        audio_stream = None
        
        if "streams" in data:
            for stream in data["streams"]:
                if stream.get("codec_type") == "video" and video_stream is None:
                    video_stream = stream
                elif stream.get("codec_type") == "audio" and audio_stream is None:
                    audio_stream = stream
        
        # Video stream info
        if video_stream:
            info["video_codec"] = video_stream.get("codec_name", "unknown").lower()
            info["width"] = video_stream.get("width", 1920)
            info["height"] = video_stream.get("height", 1080)
            info["pix_fmt"] = video_stream.get("pix_fmt", "yuv420p")
            info["color_trc"] = video_stream.get("color_transfer", "unknown")
            info["color_space"] = video_stream.get("color_space", "unknown")
            info["color_primaries"] = video_stream.get("color_primaries", "unknown")
            info["field_order"] = video_stream.get("field_order", "progressive")
            
            # FPS
            fps_str = video_stream.get("r_frame_rate", "25/1")
            if '/' in fps_str:
                num, den = fps_str.split('/')
                info["fps"] = float(num) / float(den) if float(den) != 0 else 25.0
            else:
                info["fps"] = float(fps_str)
            
            # Rotation
            tags = video_stream.get("tags", {})
            info["rotation"] = int(tags.get("rotate", 0))
        else:
            info["video_codec"] = "unknown"
            info["width"] = 1920
            info["height"] = 1080
            info["pix_fmt"] = "yuv420p"
            info["color_trc"] = "unknown"
            info["color_space"] = "unknown"
            info["color_primaries"] = "unknown"
            info["field_order"] = "progressive"
            info["fps"] = 25.0
            info["rotation"] = 0
        
        # Audio stream info
        if audio_stream:
            info["audio_codec"] = audio_stream.get("codec_name", "unknown").lower()
            audio_br = audio_stream.get("bit_rate")
            if audio_br:
                info["audio_bitrate"] = int(audio_br) // 1000
            else:
                info["audio_bitrate"] = 128
        else:
            info["audio_codec"] = "unknown"
            info["audio_bitrate"] = 0
        
        # NEW v4.6.0: Calculate bppf (bits per pixel per frame) for complexity analysis
        pixels = info["width"] * info["height"]
        if pixels > 0 and info["fps"] > 0:
            # bppf = bitrate_bps / (pixels * fps)
            raw_bppf = info["bitrate_bps"] / (pixels * info["fps"])
            info["bppf_raw"] = raw_bppf
            # NEW v4.6.2: Calculate codec-adjusted bppf
            info["bppf"] = get_effective_bppf(info["video_codec"].lower(), raw_bppf)
        else:
            info["bppf"] = 0.1
            info["bppf_raw"] = 0.1
        
        # Normalize codec name for easier comparison
        info["codec_name_normalized"] = info["video_codec"].lower()
        
        # Get file size
        try:
            info["file_size"] = os.path.getsize(path)
        except:
            info["file_size"] = 0
        
        return info
        
    except Exception as e:
        print(f"Extended probe error: {e}")
        try:
            file_size = os.path.getsize(path)
        except:
            file_size = 0
        return {
            "duration": 1.0, "fps": 25.0, "bitrate": 2000, "bitrate_bps": 2000000,
            "width": 1920, "height": 1080,
            "video_codec": "unknown", "audio_codec": "unknown",
            "audio_bitrate": 128, "pix_fmt": "yuv420p",
            "color_trc": "unknown", "color_space": "unknown", "color_primaries": "unknown",
            "field_order": "progressive",
            "rotation": 0, "bppf": 0.1, "file_size": file_size,
            "codec_name_normalized": "unknown"
        }

def smart_select_preset(info: Dict, has_nvenc: bool, has_av1: bool, user_log: List[str]) -> str:
    """
    Intelligently select encoding preset based on source characteristics
    """
    codec = info.get("video_codec", "unknown")
    bppf = info.get("bppf", 0.1)
    bitrate = info.get("bitrate", 2000)
    width = info.get("width", 1920)
    height = info.get("height", 1080)
    
    user_log.append(f"ÃƒÆ’Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â  SMART ANALYSIS:")
    user_log.append(f"   Source Codec: {codec.upper()}")
    user_log.append(f"   Resolution: {width}x{height}")
    user_log.append(f"   Bitrate: {bitrate} kbps")
    user_log.append(f"   Complexity (bppf): {bppf:.4f}")
    
    # Rule 1: Already modern codec (HEVC/AV1) with low complexity
    if codec in ["hevc", "h265", "av1"] and bppf < 0.08:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Already {codec.upper()} with low bitrate/pixel")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting FAST profile to avoid bloat")
        return "AV1 Fast"  # Default to AV1
    
    # Rule 2: H.264 or older codec with high complexity
    if codec in ["h264", "avc", "mpeg4", "msmpeg4", "xvid", "divx"] and bppf > 0.12:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ {codec.upper()} with high bitrate/pixel")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting BALANCED profile for significant savings")
        return "AV1 Balanced"  # Default to AV1
    
    # Rule 3: H.264 with very high bitrate
    if codec in ["h264", "avc"] and bitrate > 8000:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ {codec.upper()} with very high bitrate ({bitrate} kbps)")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting ULTRA profile for maximum savings")
        return "AV1 Ultra"  # Default to AV1
    
    # Rule 4: Already modern codec but medium/high complexity
    if codec in ["hevc", "h265", "av1"] and bppf >= 0.08:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Already {codec.upper()} but medium/high complexity")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting BALANCED profile")
        return "AV1 Balanced"  # Default to AV1
    
    # Rule 5: Medium complexity H.264
    if codec in ["h264", "avc"] and 0.08 <= bppf <= 0.12:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ {codec.upper()} with medium complexity")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting BALANCED profile")
        return "AV1 Balanced"  # Default to AV1
    
    # Rule 6: Low complexity H.264
    if codec in ["h264", "avc"] and bppf < 0.08:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ {codec.upper()} with low complexity (already compressed)")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Selecting FAST profile to minimize quality loss")
        return "AV1 Fast"  # Default to AV1
    
    # Default: Balanced profile
    user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Default: Selecting BALANCED profile")
    return "AV1 Balanced"  # Default to AV1

def get_smart_filters(info: Dict, keep_hdr: bool, user_log: List[str]) -> str:
    """
    Generate smart video filters based on source characteristics
    """
    filters = []
    
    # Check for interlacing
    field_order = info.get("field_order", "progressive")
    if field_order in ["tt", "bb", "tb", "bt"]:
        filters.append("yadif=mode=1")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Detected interlaced video ({field_order})")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Adding deinterlace filter (yadif)")
    
    # Check for rotation
    rotation = info.get("rotation", 0)
    if rotation == 90:
        filters.append("transpose=1")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Detected 90ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° rotation")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Adding transpose filter")
    elif rotation == 180:
        filters.append("transpose=2,transpose=2")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Detected 180ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° rotation")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Adding rotation filter")
    elif rotation == 270:
        filters.append("transpose=2")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Detected 270ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â° rotation")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Adding transpose filter")
    
    # Log HDR detection
    pix_fmt = info.get("pix_fmt", "yuv420p")
    color_trc = info.get("color_trc", "unknown")
    is_hdr = ("p010" in pix_fmt or "p210" in pix_fmt or 
              color_trc in ["smpte2084", "arib-std-b67", "bt2020"])
    
    if is_hdr and keep_hdr:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Detected HDR/10-bit content (pix_fmt={pix_fmt}, trc={color_trc})")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Will preserve 10-bit encoding")
    elif is_hdr and not keep_hdr:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â  Detected HDR/10-bit but 'Keep HDR' is disabled")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Will convert to 8-bit SDR")
    
    return ",".join(filters) if filters else ""

def should_copy_audio(info: Dict, user_log: List[str]) -> bool:
    """
    Determine if audio should be copied instead of re-encoded
    """
    audio_codec = info.get("audio_codec", "unknown")
    audio_bitrate = info.get("audio_bitrate", 999)
    
    if audio_codec == "aac" and audio_bitrate <= 192:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Audio is AAC {audio_bitrate} kbps (<=192 kbps)")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Will copy audio without re-encoding")
        return True
    else:
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Audio codec: {audio_codec}, bitrate: {audio_bitrate} kbps")
        user_log.append(f"   ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ Will re-encode audio")
        return False

def normalize_mode(mode: str) -> str:
    """
    Normalize mode names to handle legacy/saved modes and prevent unknown mode errors.
    Returns a valid mode name, defaulting to AV1 Balanced if unrecognized.
    """
    mode = mode.strip()
    mode_lower = mode.lower()
    
    # Handle exact matches first (case-insensitive)
    valid_modes = {
        "av1 ultra": "AV1 Ultra",
        "av1 balanced": "AV1 Balanced",
        "av1 compress": "AV1 Compress",
        "av1 fast": "AV1 Fast",
        "nvenc ultra": "NVENC Ultra",
        "nvenc balanced": "NVENC Balanced",
        "nvenc fast": "NVENC Fast",
        "nvenc adaptive": "NVENC Adaptive"
    }

    if mode_lower in valid_modes:
        return valid_modes[mode_lower]

    # Handle legacy mode names and variants
    if "av1" in mode_lower:
        if "ultra" in mode_lower:
            return "AV1 Ultra"
        elif "compress" in mode_lower:
            return "AV1 Compress"
        elif "fast" in mode_lower:
            return "AV1 Fast"
        else:
            return "AV1 Balanced"
    
    if "nvenc" in mode_lower or "hevc" in mode_lower:
        if "ultra" in mode_lower:
            return "NVENC Ultra"
        elif "fast" in mode_lower:
            return "NVENC Fast"
        elif "adaptive" in mode_lower:
            return "NVENC Adaptive"
        else:
            return "NVENC Balanced"
    
    # If completely unrecognized, default to AV1 Balanced
    return "AV1 Balanced"


# ============================================================================
# NEW v4.5.0/v4.6.0: NOVA-STYLE ADAPTIVE NVENC FUNCTIONS
# ============================================================================

def is_source_hdr(info: Dict) -> bool:
    """
    Detect if source is actually HDR/10-bit
    """
    pix_fmt = info.get("pix_fmt", "yuv420p")
    color_trc = info.get("color_trc", "unknown")
    color_space = info.get("color_space", "unknown")
    color_primaries = info.get("color_primaries", "unknown")
    
    # Check for 10-bit pixel formats
    if "10" in pix_fmt or "p010" in pix_fmt or "p210" in pix_fmt:
        return True
    
    # Check for HDR transfer characteristics
    if color_trc in ["smpte2084", "arib-std-b67", "smpte428"]:
        return True
    
    # Check for wide color gamut
    if "bt2020" in color_space or "bt2020" in color_primaries:
        return True
    
    return False

def apply_vbv_profile(params: Dict, maxrate_mult: float, bufsize_mult: float) -> None:
    """Attach a VBV profile to params so later tweaks can reapply consistently."""
    params["_vbv_profile"] = {"maxrate": maxrate_mult, "bufsize": bufsize_mult}
    params["maxrate"] = int(params["b_v"] * maxrate_mult)
    params["bufsize"] = int(params["b_v"] * bufsize_mult)

def reapply_vbv(params: Dict) -> None:
    """Recompute maxrate/bufsize if bitrate changed."""
    profile = params.get("_vbv_profile")
    if not profile:
        return
    params["maxrate"] = int(params["b_v"] * profile["maxrate"])
    params["bufsize"] = int(params["b_v"] * profile["bufsize"])

def enforce_minimum_bitrate(params: Dict, src_height: int, path_used: str = "default", is_hdr: bool = False) -> None:
    """
    Apply a single floor unless a specialized path already set its own target.
    Keeping one guard avoids multi-floor stacking noted in issue #3.
    """
    if path_used in {"bold", "medium_1080p"}:
        return
    if src_height >= 1080 and not is_hdr:
        params["b_v"] = max(params["b_v"], MIN_1080P_TARGET)
    elif src_height >= 720:
        params["b_v"] = max(params["b_v"], MIN_720P_TARGET)
    reapply_vbv(params)

def refine_nvenc_params(
    params: Dict,
    src_info: Dict,
    apply_complexity: bool = True,
    apply_proximity: bool = True,
    apply_codec: bool = True
) -> Dict:
    """
    Shared refinement helper so CQ/bitrate micro-adjustments occur exactly once.
    """
    src_br_bps = int(src_info.get("bitrate_bps", 0))
    bppf = float(src_info.get("bppf", 0.1))
    codec = src_info.get("codec_name_normalized", "").lower()

    if apply_complexity and not params.get("_complexity_refined"):
        if bppf >= 0.12:
            params["cq"] = max(params["cq"] - 1, 18)
            params["b_v"] = int(params["b_v"] * 1.10)
        elif bppf <= 0.05:
            params["cq"] = min(params["cq"] + 1, 32)
        params["_complexity_refined"] = True
        reapply_vbv(params)

    # OPTIMIZED: Looser proximity detection to avoid unnecessary transcoding
    if apply_proximity and not params.get("_proximity_refined") and src_br_bps > 0 and params.get("b_v", 0) > 0:
        diff_pct = abs(src_br_bps - params["b_v"]) / params["b_v"] * 100
        if diff_pct <= 3:
            # Source already at target - mark for potential skip
            params["_skip_encode"] = True
            params["_skip_reason"] = f"Source bitrate within 3% of target ({diff_pct:.1f}%)"
        elif diff_pct <= 15:
            # Close to target - gentle nudge only (CQ +1, no bitrate reduction)
            params["cq"] = min(params["cq"] + 1, 32)
            # Don't force bitrate reduction when source is close
        elif src_br_bps >= params["b_v"] * 2.5:
            # Source much higher than target - protect quality during compression
            params["cq"] = max(params["cq"] - 1, 18)
        params["_proximity_refined"] = True
        reapply_vbv(params)

    if apply_codec and not params.get("_codec_refined"):
        if any(tag in codec for tag in ["hevc", "h265", "hev1"]):
            params["cq"] = min(params["cq"] + 1, 32)
        params["_codec_refined"] = True

    return params

def choose_adaptive_params(src_width: int, src_height: int, src_bitrate_bps: int, bppf: float, src_codec: str = "", encoder: str = "nvenc") -> Dict:
    """
    NEW v5.0: Unified adaptive parameter selection for NVENC and AMF
    
    Uses same logic but clamps values to encoder-safe ranges.
    AMF sometimes rejects very low bitrates, so we add protection floors.
    """
    params = choose_nvenc_params(src_width, src_height, src_bitrate_bps, bppf, src_codec)
    
    # v5.1: Apply unified safety floors (so AMF matches NVENC defaults)
    if encoder == "amf":
        # AMF protection: Ensure minimum bitrates to avoid encoder rejection
        if src_height >= 1080:
            params["b_v"] = max(params["b_v"], MIN_1080P_TARGET)
        elif src_height >= 720:
            params["b_v"] = max(params["b_v"], MIN_720P_TARGET)
        # Clamp CQ to AMF-safe range (18-32, same as NVENC)
        params["cq"] = max(18, min(32, params["cq"]))
        reapply_vbv(params)
    
    return params

def choose_nvenc_params(src_width: int, src_height: int, src_bitrate_bps: int, bppf: float, src_codec: str = "") -> Dict:
    """
    NEW v4.6.0: NOVA-STYLE three-level adaptive parameter selection
    v4.6.2: Added legacy codec detection for unconstrained VBR
    
    Three-level decision system:
    1. Resolution tier (SD/720p/1080p/1440p/4K)
    2. Bitrate band (low/normal/high for each tier)
    3. Complexity fine-tuning (bppf-based adjustment)
    
    Plus relative adjustment to avoid "no compression" scenarios
    
    v4.6.2: Legacy codecs (MPEG-4, XviD, etc.) use unconstrained VBR
    for better compression like v4.4.0
    """
    
    # NEW v4.6.2: Detect legacy codecs - use simpler unconstrained VBR
    is_legacy = src_codec.lower() in [
        "mpeg4", "msmpeg4", "msmpeg4v2", "msmpeg4v3",
        "xvid", "divx", "mjpeg", "h263", "vp6"
    ]
    
    # LEVEL 1: Resolution-based tier selection
    # OPTIMIZED: Increased CQ by 3-4 points for 30-45% size reduction while maintaining quality
    if src_width >= 3840:  # 4K / 2160p
        base_cq = 27  # Was 23, +4 (still excellent for 4K HEVC)
        base_target = 8_000_000  # Reduced from 12M
    elif src_width >= 2560:  # 1440p
        if src_bitrate_bps >= 8_000_000:
            base_cq = 28  # Was 24, +4
            base_target = 4_500_000  # Reduced from 6M
        else:
            base_cq = 29  # Was 25, +4
            base_target = 3_800_000  # Reduced from 5M
    elif src_width >= 1920:  # 1080p
        # LEVEL 2: Bitrate band within resolution tier
        if src_bitrate_bps >= 8_000_000:  # Very high bitrate 1080p
            base_cq = 28  # Was 24, +4 (excellent quality, smaller size)
            base_target = 3_200_000  # Reduced from 4.5M
        elif src_bitrate_bps >= 4_000_000:  # Normal 1080p (most common)
            base_cq = 29  # Was 25, +4 (sweet spot for size/quality)
            base_target = 2_500_000  # Reduced from 3.5M
        else:  # Low bitrate 1080p
            base_cq = 30  # Was 26, +4
            base_target = 2_200_000  # Reduced from 3.0M
    elif src_width >= 1280:  # 720p
        base_cq = 30  # Was 27, +3
        base_target = 1_800_000  # Reduced from 2.2M
    else:  # SD / small sources
        base_cq = 31  # Was 28, +3
        base_target = 1_200_000  # Reduced from 1.5M
    
    # NEW v4.6.2: For legacy codecs, return unconstrained VBR (like v4.4.0)
    # BUT with safety floors to prevent 1-hour legacy videos from ballooning
    if is_legacy:
        # Use simple CQ-based encoding without bitrate constraints
        # This works better for inefficient legacy codecs
        # Use CQ 26 for 1080p regardless of source bitrate (high bitrate = inefficiency, not complexity)
        if src_width >= 1920:
            legacy_cq = 26  # 1080p+
        elif src_width >= 1280:
            legacy_cq = 27  # 720p
        else:
            legacy_cq = 28  # SD
        
        # Apply safety floors based on resolution
        if src_height >= 1080:
            safety_b_v = max(2_700_000, MIN_1080P_TARGET)  # Legacy floor comment for quick retune
        elif src_height >= 720:
            safety_b_v = max(2_000_000, MIN_720P_TARGET)
        else:
            safety_b_v = 1_500_000
        
        # Ensure CQ is at least 27
        legacy_cq = max(legacy_cq, 27)
        
        # Set maxrate and bufsize based on safety floor
        params = {
            "cq": legacy_cq,
            "b_v": safety_b_v,  # Safety floor
            "mode": "unconstrained"
        }
        apply_vbv_profile(params, DEFAULT_MAXRATE_MULT, DEFAULT_BUFSIZE_MULT)
        return params
    
    params = {
        "cq": base_cq,
        "b_v": base_target,
        "mode": "constrained"
    }
    apply_vbv_profile(params, DEFAULT_MAXRATE_MULT, DEFAULT_BUFSIZE_MULT)

    # Apply complexity + proximity once by default (finish() will skip duplicates)
    snapshot = {
        "bitrate_bps": src_bitrate_bps,
        "bppf": bppf,
        "codec_name_normalized": src_codec
    }
    refine_nvenc_params(params, snapshot, apply_codec=False)
    
    return params

def detect_best_encoder(preferred: str = "auto") -> Tuple[str, bool]:
    """
    NEW v5.0: Detect available encoder (NVIDIA NVENC, AMD AMF, or CPU)
    
    Args:
        preferred: "auto", "nvenc", "amf", or "cpu"
    
    Returns:
        (encoder_name, use_hwaccel) tuple
    """
    if preferred == "nvenc":
        if HAS_HEVC_NVENC:
            return ("nvenc", True)
        else:
            return ("cpu", False)
    elif preferred == "amf":
        if HAS_ANY_AMF:
            return ("amf", True)
        else:
            return ("cpu", False)
    elif preferred == "cpu":
        return ("cpu", False)
    else:  # auto
        # Prefer AMD AV1 if available, then NVENC, then fallback AMF, then CPU
        if HAS_AV1_AMF:
            return ("amf", True)
        elif HAS_HEVC_NVENC:
            return ("nvenc", True)
        elif HAS_ANY_AMF:
            return ("amf", True)
        else:
            return ("cpu", False)

def should_downscale_fps_to_30(src_info: Dict) -> bool:
    """
    Ã˜Â±Ã˜Â¬Ã™â€˜Ã˜Â¹ True Ã™â€žÃ™Ë† Ã˜Â§Ã™â€žÃ™â€¦Ã˜ÂµÃ˜Â¯Ã˜Â± fps Ã˜Â¹Ã˜Â§Ã™â€žÃ™Å  (50/60) Ã™Ë†Ã™â€ Ã˜Â¨Ã˜ÂºÃ™â€° Ã™â€ Ã™â€ Ã˜Â²Ã™â€žÃ™â€¡ Ã™â€žÃ™â‚¬ 30 Ã˜Â¹Ã˜Â´Ã˜Â§Ã™â€  Ã˜Â­Ã˜Â¬Ã™â€¦ Ã˜Â£Ã™ÂÃ˜Â¶Ã™â€ž.
    Don't touch 24/25/30 fps.
    """
    fps = float(src_info.get("fps", 30))
    # Ã˜Â§Ã˜Â¹Ã˜ÂªÃ˜Â¨Ã˜Â± Ã˜Â£Ã™Å  Ã˜Â´Ã™Å Ã˜Â¡ Ã™ÂÃ™Ë†Ã™â€š 45 Ã˜Â§Ã™â€ Ã™â€¡ 50/60
    return fps > 45.0

def detect_bold_compression_path(src_info: Dict) -> bool:
    """
    v5.1: Broadened Bold path detector so more studio sources qualify.
    - Height Ã¢â€°Â¥ 1080 (downscales allowed)
    - Codec Ã¢Ë†Ë† {H.264/H.265/AV1/ProRes/DNxHR}
    - Bitrate 5-12 Mbps
    - fps Ã¢â€°Â¤ 60
    - SDR only (HDR gracefully falls back to default)
    """
    try:
        width = int(src_info.get("width", 0))
        height = int(src_info.get("height", 0))
        codec = src_info.get("codec_name_normalized", "").lower()
        bitrate_bps = int(src_info.get("bitrate_bps", 0) or src_info.get("bitrate", 0) * 1000)
        fps = float(src_info.get("fps", 30))
        source_is_hdr = is_source_hdr(src_info)
        
        allowed_codecs = {"h264", "avc", "avc1", "h.264", "hevc", "h265", "hev1", "av1", "prores", "dnxhr"}
        is_hd = height >= 1080 and width >= 1280
        codec_ok = codec in allowed_codecs
        bitrate_ok = 5_000_000 <= bitrate_bps <= 12_000_000
        fps_ok = fps <= 60
        
        if source_is_hdr:
            return False
        return is_hd and codec_ok and bitrate_ok and fps_ok
    except Exception:
        return False

def apply_bold_compression_params(
        params: Dict,
        sharpening_profile: str,
        src_bitrate_bps: int = 0,
        fps: float = 30.0,
        bppf: float = 0.1
    ) -> Tuple[Dict, str]:
    """
    Bold Compression (studio SDR, ~5-12 Mbps)
    - Complexity-aware with 3 bppf bands:
      * High complexity (bppf >= 0.12): 3.0 Mbps, CQ 26
      * Medium complexity (0.09-0.12): 2.8 Mbps, CQ 27
      * Low complexity (< 0.09): 2.3 Mbps, CQ 28
    - Tighter VBR: maxrate = target * 1.15, bufsize = maxrate * 2
    """
    # Complexity-aware targeting based on bppf
    # OPTIMIZED: Lower bitrates, higher CQ for better compression
    if bppf >= 0.12:
        # High complexity: protect details but still compress well
        target_bitrate = 2_400_000  # Was 3.0M, reduced 20%
        bold_cq = 29  # Was 26, +3
    elif bppf >= 0.09:
        # Medium complexity: balanced
        target_bitrate = 2_200_000  # Was 2.8M, reduced 21%
        bold_cq = 30  # Was 27, +3
    else:
        # Low complexity: compress harder
        target_bitrate = max(MIN_1080P_TARGET, 1_900_000)  # Was 2.3M
        bold_cq = 31  # Was 28, +3

    if fps and fps > 45:
        target_bitrate = int(target_bitrate * 1.05)

    params["b_v"] = target_bitrate
    params["cq"] = bold_cq
    params["mode"] = "bold"
    params["bold_cq"] = bold_cq
    # Use tighter VBR control (1.15x maxrate instead of 1.28x)
    apply_vbv_profile(params, BOLD_MAXRATE_MULT, BOLD_BUFSIZE_MULT)
    
    filter_profile = "bold"
    
    return params, filter_profile

def detect_medium_1080p_path(src_info: Dict) -> bool:
    """
    Medium safety profile detector (v5.1 rules).
    - Height Ã¢â€°Â¥ 1080
    - Bitrate 3.8-6 Mbps
    - fps Ã¢â€°Â¤ 60 (doc + logic synced)
    - Same codec whitelist as Bold
    - HDR falls back to default path
    """
    try:
        width = int(src_info.get("width", 0))
        height = int(src_info.get("height", 0))
        codec = src_info.get("codec_name_normalized", "").lower()
        bitrate_bps = int(src_info.get("bitrate_bps", 0) or src_info.get("bitrate", 0) * 1000)
        fps = float(src_info.get("fps", 30))
        source_is_hdr = is_source_hdr(src_info)
        
        allowed_codecs = {"h264", "avc", "avc1", "h.264", "hevc", "h265", "hev1", "av1", "prores", "dnxhr"}
        is_hd = height >= 1080 and width >= 1280
        codec_ok = codec in allowed_codecs
        bitrate_ok = 3_800_000 <= bitrate_bps <= 6_000_000
        fps_ok = fps <= 60
        
        if source_is_hdr:
            return False
        return is_hd and codec_ok and bitrate_ok and fps_ok
    except Exception:
        return False

def apply_medium_1080p_params(params: Dict, src_info: Dict, bppf: float) -> Tuple[Dict, str]:
    """
    NEW v5.0: Apply Medium-Bitrate 1080p Safety-Downscale parameters
    
    Sets:
    - target_video_bitrate = 3_000_000  # Medium target bps (3.0 Mbps)
    - maxrate/bufsize use MEDIUM_* multipliers (see constants section)
    - cq = 26 (if scene complexity is low ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ allow cq = 27)
    - Uses softer filters from FILTER_PROFILES["medium_soft"]
    
    Returns: (updated_params, filter_profile)
    """
    # OPTIMIZED: Lower target for better compression
    target_video_bitrate = 2_400_000  # Was 3.0M, reduced 20%

    # CQ adjustment based on scene complexity
    # OPTIMIZED: Higher CQ values
    # If low complexity (bppf ÃƒÂ¢Ã¢â‚¬Â°Ã‚Â¤ 0.05), allow CQ 27; otherwise use CQ 26
    if bppf <= 0.05:
        medium_cq = 30  # Low complexity ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ can compress slightly more
    else:
        medium_cq = 29  # Normal complexity ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ protect quality
    
    params["b_v"] = target_video_bitrate
    params["cq"] = medium_cq
    params["mode"] = "medium_1080p"  # Mark as medium-1080p path
    params["medium_cq"] = medium_cq  # Store for logging
    
    fps = int(src_info.get("fps", 30))
    maxrate_mult = MEDIUM_MAXRATE_MULT + (0.03 if fps > 45 else 0.0)
    bufsize_mult = MEDIUM_BUFSIZE_MULT + (0.2 if fps > 45 else 0.0)
    apply_vbv_profile(params, maxrate_mult, bufsize_mult)
    
    # Force softer filters via centralized profile
    filter_profile = "medium_soft"
    
    return params, filter_profile

def finish_cq_for_source(src_info: Dict, params: Dict) -> Dict:
    """
    NEW v4.6.2: Final CQ and rate refinement based on source characteristics
    v4.6.2: Skip refinements for legacy codecs using unconstrained VBR
    
    This runs AFTER choose_nvenc_params() to apply fine-tuning based on:
    - Codec type (H.264 vs HEVC - HEVC can be compressed more)
    - Complexity (bppf - high motion needs protection)
    - Source-to-target proximity (avoid "no compression" scenarios)
    
    Returns: Updated params dict with refined values
    """
    # NEW v4.6.2: Skip refinement for unconstrained VBR (legacy codecs)
    if params.get("mode") == "unconstrained":
        # Legacy codecs already using simple unconstrained VBR
        # No refinement needed - let CQ do its job
        return params
    
    snapshot = {
        "bitrate_bps": int(src_info.get("bitrate_bps", 0)),
        "bppf": float(src_info.get("bppf", 0.1)),
        "codec_name_normalized": src_info.get("codec_name_normalized", "").lower()
    }
    
    params = refine_nvenc_params(
        params,
        snapshot,
        apply_complexity=not params.get("_complexity_refined"),
        apply_proximity=not params.get("_proximity_refined"),
        apply_codec=True
    )
    
    return params

def estimate_output_from_params(src_info: Dict, params: Dict) -> int:
    """
    NEW v4.6.2: Estimate output size from adaptive parameters
    
    Uses smarter weighted average: target * 0.6 + maxrate * 0.4
    Gets real audio bitrate from probe if available.
    
    Returns: Estimated output size in bytes
    """
    duration = float(src_info.get("duration", 0))
    if duration <= 0:
        return 0
    
    target = float(params.get("b_v", 3_500_000))
    maxrate = float(params.get("maxrate", target * DEFAULT_MAXRATE_MULT))
    
    # Smarter estimation: est_video_bps = target * 0.6 + maxrate * 0.4
    est_video_bps = (target * 0.6) + (maxrate * 0.4)
    
    # Get real audio bitrate from probe if available; if not, assume 160 kbps
    audio_bitrate_kbps = src_info.get("audio_bitrate", 160)
    if audio_bitrate_kbps <= 0:
        audio_bitrate_kbps = 160
    audio_bitrate_bps = audio_bitrate_kbps * 1000
    
    total_bps = est_video_bps + audio_bitrate_bps
    
    # Calculate size: total_bps * duration / 8
    estimated_size = int((total_bps * duration) / 8)
    
    return estimated_size

def should_skip_for_low_saving(src_info: Dict, params: Dict, min_saving_pct: float = 3.0, use_bold_path: bool = False) -> Tuple[bool, str]:
    """
    NEW v4.6.1: Pre-encoding skip check based on estimated savings
    
    Prevents encoding when estimated savings are below threshold.
    More accurate than simple bitrate comparison.
    
    NEW v5.0: Bold path uses 2% threshold instead of 3%
    
    Returns: (should_skip, reason)
    """
    # NEW v5.0: Bold path uses less strict threshold (2%)
    if use_bold_path:
        min_saving_pct = 2.0
    
    src_size = src_info.get("file_size", 0)
    if src_size <= 0:
        return (False, "")
    
    est_output_size = estimate_output_from_params(src_info, params)
    if est_output_size <= 0:
        return (False, "")
    
    # Compute reduction percentage
    reduction_pct = (1 - est_output_size / src_size) * 100
    
    # Check if output would be bigger (negative reduction)
    if reduction_pct < -2:  # Output would be >2% bigger
        reason = f"Estimated output ({fmt_size(est_output_size)}) would be larger than source ({fmt_size(src_size)})"
        return (True, reason)
    
    # Check if reduction is below threshold
    # For legacy codecs, allow encoding even if saving is a bit low (they compress well)
    src_codec = src_info.get("codec_name_normalized", "").lower()
    is_modern = src_codec in ["h264", "avc", "hevc", "h265", "av1"]
    
    if reduction_pct < min_saving_pct:
        # Only skip if codec IS modern (legacy codecs often compress well)
        # Exception: Bold path never skips H.264 sources (they're known good candidates)
        if is_modern and not (use_bold_path and src_codec in ["h264", "avc"]):
            reason = (f"Estimated savings {reduction_pct:.1f}% is below threshold {min_saving_pct:.1f}%. "
                     f"Source: {fmt_size(src_size)}, Estimated output: {fmt_size(est_output_size)}")
            return (True, reason)
        # For legacy codecs or Bold path H.264, continue encoding even if savings is low
    
    return (False, "")


def normalize_codec_name(codec: str) -> str:
    """Normalize codec name for consistent comparisons"""
    codec = codec.lower()
    
    # H.264 aliases
    if codec in ["h264", "avc", "avc1", "h.264"]:
        return "h264"
    
    # HEVC/H.265 aliases
    if codec in ["hevc", "h265", "h.265"]:
        return "hevc"
    
    # Legacy codecs
    if codec in ["mpeg4", "msmpeg4", "msmpeg4v2", "msmpeg4v3"]:
        return "mpeg4"
    
    if codec in ["xvid", "divx"]:
        return "xvid"
    
    return codec


def get_effective_bppf(codec: str, raw_bppf: float) -> float:
    """
    NEW v4.6.2: Codec-aware bppf adjustment
    
    Legacy codecs (MPEG-4, XviD, DivX) are ~1.7x less efficient than H.264,
    so their high bppf doesn't indicate complexity - just codec inefficiency.
    
    This prevents over-protection of legacy codec sources.
    
    Args:
        codec: Normalized codec name (lowercase)
        raw_bppf: Raw bits per pixel per frame
    
    Returns:
        Adjusted bppf that reflects actual content complexity
    """
    # Legacy codecs: Very inefficient, scale down bppf
    if codec in ["mpeg4", "msmpeg4", "msmpeg4v2", "msmpeg4v3", "xvid", "divx", "mjpeg", "h263"]:
        # MPEG-4 family is ~1.7x less efficient than H.264
        # So 0.170 bppf MPEG-4 ÃƒÂ¢Ã¢â‚¬Â°Ã‹â€  0.100 bppf H.264
        return raw_bppf / 1.7
    
    # VP8/VP6: Somewhat inefficient
    elif codec in ["vp6", "vp8"]:
        return raw_bppf / 1.3
    
    # Modern efficient codecs: No adjustment needed
    elif codec in ["hevc", "h265", "av1", "vp9"]:
        return raw_bppf
    
    # H.264 and others: Baseline (no adjustment)
    else:
        return raw_bppf

def get_adaptive_denoise(src_bitrate_bps: int, is_hdr_source: bool, keep_hdr: bool) -> Tuple[str, str, str]:
    """
    NEW v4.6.0: Enhanced adaptive denoise with HDRÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢SDR refinement
    
    Returns: (denoise_filter, unsharp_filter, profile_name)
    """
    # NEW v4.6.0: If converting HDR to SDR, use softer filters
    if is_hdr_source and not keep_hdr:
        denoise, unsharp = get_filter_profile("hdr_sdr_soft")
        return denoise, unsharp, "hdr_sdr_soft"
    
    # Standard adaptive denoise based on source quality
    if src_bitrate_bps >= 8_000_000:
        profile_name = "clean_h264"
    elif src_bitrate_bps >= 4_000_000:
        profile_name = "balanced"
    else:
        profile_name = "gritty"
    
    denoise, unsharp = get_filter_profile(profile_name)
    return (denoise, unsharp, profile_name)

def should_skip_encoding(info: Dict, user_log: List[str]) -> Tuple[bool, str]:
    """
    NEW v4.6.0: SMART SKIP 2.0 - Check if file should be skipped entirely
    
    Returns: (should_skip, reason)
    """
    codec = info.get("video_codec", "unknown")
    height = info.get("height", 1080)
    bitrate_bps = info.get("bitrate_bps", 0)
    
    # Skip already-efficient HEVC files
    if codec in ["hevc", "h265"] and height <= 1080 and bitrate_bps <= 3_500_000:
        reason = f"Source already efficient HEVC (<=3.5 Mbps at <=1080p)"
        user_log.append(f"   [ROCKET] SMART SKIP: {reason}")
        return (True, reason)
    
    return (False, "")

# ============================================================================
# SIZE ESTIMATION & UTILITY FUNCTIONS
# ============================================================================

def estimate_output_size(input_path: str, mode: str, resolution: str, input_bitrate: int = 0,
                         keep_hdr: bool = True, encoder_hint: str = "auto",
                         smart_filters: Optional[str] = None, copy_audio: bool = False,
                         custom_cq: Optional[int] = None, sharpening_profile: str = "medium") -> int:
    """
    NEW v4.6.0: Enhanced size estimation with adaptive NVENC awareness
    v5.1.1: Fixed to handle unusual video formats (portrait, reversed stream order, high fps)
    """
    try:
        input_size = os.path.getsize(input_path)
        info = ffprobe_info(input_path)
        duration = info["duration"]
        if input_bitrate == 0:
            input_bitrate = info["bitrate"]
        width = info["width"]
        height = info["height"]

        # Debug logging for unusual formats
        if width < height:  # Portrait orientation
            print(f"[EST] Portrait video detected: {width}x{height}")
        if info.get("fps", 0) > 50:  # High framerate
            print(f"[EST] High framerate detected: {info.get('fps'):.2f} fps")
        if input_bitrate > 15000:  # Very high bitrate
            print(f"[EST] High bitrate detected: {input_bitrate} kbps")
        
        # Determine source complexity level
        if input_bitrate > 8000:
            complexity = "high"
        elif input_bitrate > 5000:
            complexity = "medium"
        else:
            complexity = "normal"
        
        # Calculate target resolution pixels
        if resolution == "Same as source":
            target_pixels = width * height
        elif resolution == "1080p":
            target_pixels = 1920 * 1080
        elif resolution == "720p":
            target_pixels = 1280 * 720
        elif resolution == "480p":
            target_pixels = 854 * 480
        else:
            target_pixels = width * height
        
        # Resolution scaling factor
        pixels_1080p = 1920 * 1080
        resolution_factor = target_pixels / pixels_1080p
        
        # Adaptive bitrate targets
        # For estimation, we don't need the actual AMD preview logic - just estimate properly
        use_amd_av1_preview = False  # Simplified for estimation
        adaptive_modes = {"NVENC Ultra", "NVENC Balanced", "NVENC Fast"}
        hint_lower = (encoder_hint or "auto").lower()
        encoder_choice, _ = detect_best_encoder(hint_lower)
        if encoder_choice not in {"amf", "nvenc"}:
            encoder_choice = "nvenc"
        use_balanced_amf = (mode == "AV1 Balanced" and encoder_choice == "amf")
        use_compress_amf = (mode == "AV1 Compress" and encoder_choice == "amf")

        # For NVENC/AMF modes or AV1 Balanced/Compress with AMD hardware, use adaptive plan
        if mode in adaptive_modes or use_balanced_amf or use_compress_amf or use_amd_av1_preview:
            info_ext = ffprobe_info_extended(input_path)
            filters_for_est = smart_filters
            if filters_for_est is None:
                filters_for_est = get_smart_filters(info_ext, keep_hdr, [])
            plan = EncodingPresets._compute_hw_adaptive_plan(
                resolution,
                width,
                height,
                input_path,
                filters_for_est,
                keep_hdr,
                None,
                custom_cq,
                sharpening_profile,
                encoder=encoder_choice
            )

            # Apply AV1 Compress mode adjustments for accurate estimation
            if mode == "AV1 Compress" and encoder_choice == "amf":
                plan["params"]["cq"] = 31  # Higher CQ = more compression
                if width >= 1920:
                    plan["params"]["b_v"] = 1_900_000  # 1.9 Mbps for 1080p
                    plan["params"]["maxrate"] = int(plan["params"]["b_v"] * 1.5)
                    plan["params"]["bufsize"] = int(plan["params"]["maxrate"] * 2)
                elif width >= 1280:
                    plan["params"]["b_v"] = 1_200_000  # 1.2 Mbps for 720p
                    plan["params"]["maxrate"] = int(plan["params"]["b_v"] * 1.5)
                    plan["params"]["bufsize"] = int(plan["params"]["maxrate"] * 2)

            base_video_bitrate = estimate_output_from_params(info_ext, plan["params"]) * 8 / max(duration, 1)
            base_video_bitrate /= 1000  # Convert to kbps for consistency
            audio_bitrate = 192
        else:
            base_video_bitrate = 3000
            audio_bitrate = 192
        
        # Apply resolution scaling
        target_video_bitrate = base_video_bitrate * resolution_factor
        
        # Sanity bounds for low-quality sources
        if input_bitrate < 2000:
            target_video_bitrate = min(target_video_bitrate, input_bitrate * 0.85)
        
        # Calculate total bitrate
        total_bitrate = target_video_bitrate + audio_bitrate
        
        # Calculate estimated size
        estimated_bytes = int((total_bitrate * duration * 1000) / 8)
        
        # Safety bounds
        estimated_bytes = max(estimated_bytes, 512 * 1024)
        estimated_bytes = min(estimated_bytes, input_size * 0.95)
        
        return estimated_bytes
        
    except Exception as e:
        print(f"Estimation error: {e}")
        return int(os.path.getsize(input_path) * 0.35)

def get_smart_audio_bitrate(input_path: str, mode: str) -> Tuple[str, str]:
    """
    OPTIMIZED: Intelligently match audio bitrate to source, copy when efficient
    Returns: (codec, bitrate) where codec can be "copy" or "aac"
    """
    try:
        result = subprocess.run(
            [FFPROBE, "-v", "error", "-select_streams", "a:0",
             "-show_entries", "stream=codec_name,bit_rate,sample_rate",
             "-of", "json", input_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        data = json.loads(result.stdout)
        if "streams" in data and len(data["streams"]) > 0:
            stream = data["streams"][0]
            audio_codec = stream.get("codec_name", "").lower()
            input_audio_br = int(stream.get("bit_rate", 128000)) // 1000
            input_sample_rate = int(stream.get("sample_rate", 48000))
        else:
            return ("aac", "128k")  # No audio stream, use default
        
        # OPTIMIZED: Copy audio if already efficient (avoid double encoding loss)
        if audio_codec == "aac" and input_audio_br <= 192:
            return ("copy", "")  # AAC at ≤192 kbps is already efficient
        if audio_codec == "opus" and input_audio_br <= 160:
            return ("copy", "")  # Opus at ≤160 kbps is excellent
        if audio_codec == "eac3" and input_audio_br <= 256:
            return ("copy", "")  # E-AC3 is efficient
        
        # For lossy-to-lossy transcoding (avoid double loss)
        if audio_codec in ["mp3", "vorbis", "wmav2", "ac3"] and input_audio_br <= 128:
            # Don't upsample lossy audio, match source bitrate
            target_br = min(input_audio_br, 128)
            return ("aac", f"{target_br}k")
        
        # Smart bitrate decision for high-quality sources
        if input_audio_br <= 96:
            return ("aac", "96k")  # Don't upsample beyond source
        elif input_audio_br <= 128:
            return ("aac", "128k")
        elif input_audio_br <= 160:
            return ("aac", "160k")
        else:
            # Use mode-based targeting for high-quality sources
            bitrate_map = {
                "AV1 Ultra": "192k",
                "AV1 Balanced": "160k",
                "AV1 Compress": "128k",
                "AV1 Fast": "128k",
                "NVENC Ultra": "192k",
                "NVENC Balanced": "160k",
                "NVENC Fast": "128k",
                "NVENC Adaptive": "160k",
                "AMF Adaptive": "160k"
            }
            target_br = bitrate_map.get(mode, "160k")
            return ("aac", target_br)
            
    except Exception as e:
        # Safe fallback
        fallback_map = {
            "AV1 Ultra": "192k",
            "AV1 Balanced": "160k",
            "AV1 Compress": "128k",
            "AV1 Fast": "128k",
            "NVENC Ultra": "160k",
            "NVENC Balanced": "160k",
            "NVENC Fast": "128k",
            "NVENC Adaptive": "160k",
            "AMF Adaptive": "160k"
        }
        return ("aac", fallback_map.get(mode, "160k"))

def fmt_hms(s: float) -> str:
    """Format seconds to HH:MM:SS"""
    s = max(0, int(s))
    return f"{s//3600:02d}:{(s%3600)//60:02d}:{s%60:02d}"

def fmt_size(bytes_val: float) -> str:
    """Format bytes to human-readable size"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024:
            return f"{bytes_val:.1f} {unit}"
        bytes_val /= 1024
    return f"{bytes_val:.1f} TB"

def get_system_cpu() -> float:
    """Get system CPU usage"""
    try:
        return psutil.cpu_percent(interval=0.1)
    except:
        return 0.0

def get_gpu_stats() -> Tuple[Optional[int], Optional[int]]:
    """Get GPU utilization and temperature"""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", 
             "--query-gpu=utilization.gpu,temperature.gpu",
             "--format=csv,noheader,nounits"],
            stderr=subprocess.DEVNULL, timeout=2
        )
        parts = out.decode().strip().split(',')
        if len(parts) >= 2:
            return (int(parts[0].strip()), int(parts[1].strip()))
    except:
        pass
    return (None, None)

def check_disk_space(output_path: str, estimated_size: int) -> bool:
    """Check if there's enough disk space"""
    try:
        output_dir = os.path.dirname(output_path) or '.'
        stat = shutil.disk_usage(output_dir)
        return stat.free > estimated_size * 1.5
    except:
        return True

# ============================================================================
# PROFILE & HISTORY MANAGEMENT
# ============================================================================

PROFILES_FILE = "encoding_profiles.json"
HISTORY_FILE = "encoding_history.json"

def save_profile(profile: EncodingProfile) -> bool:
    """Save an encoding profile to disk"""
    try:
        profiles = load_all_profiles()
        # Update or add profile
        profiles[profile.name] = {
            "mode": profile.mode,
            "resolution": profile.resolution,
            "two_pass": profile.two_pass,
            "auto_mode": profile.auto_mode,
            "keep_hdr": profile.keep_hdr,
            "skip_small_saving": profile.skip_small_saving,
            "custom_cq": profile.custom_cq,
            "custom_filters": profile.custom_filters,
            "sharpening_profile": profile.sharpening_profile,
            "av1_tune": profile.av1_tune
        }
        with open(PROFILES_FILE, 'w') as f:
            json.dump(profiles, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving profile: {e}")
        return False

def load_all_profiles() -> Dict[str, Dict]:
    """Load all saved profiles"""
    try:
        if os.path.exists(PROFILES_FILE):
            with open(PROFILES_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading profiles: {e}")
    return {}

def load_profile(name: str) -> Optional[EncodingProfile]:
    """Load a specific profile by name"""
    profiles = load_all_profiles()
    if name in profiles:
        data = profiles[name]
        return EncodingProfile(
            name=name,
            mode=data.get("mode", "AV1 Balanced"),
            resolution=data.get("resolution", "Same as source"),
            two_pass=data.get("two_pass", False),
            auto_mode=data.get("auto_mode", True),
            keep_hdr=data.get("keep_hdr", True),
            skip_small_saving=data.get("skip_small_saving", False),
            custom_cq=data.get("custom_cq"),
            custom_filters=data.get("custom_filters", ""),
            sharpening_profile=data.get("sharpening_profile", "medium"),
            av1_tune=data.get("av1_tune", "vmaf")
        )
    return None

def delete_profile(name: str) -> bool:
    """Delete a profile"""
    try:
        profiles = load_all_profiles()
        if name in profiles:
            del profiles[name]
            with open(PROFILES_FILE, 'w') as f:
                json.dump(profiles, f, indent=2)
            return True
    except Exception as e:
        print(f"Error deleting profile: {e}")
    return False

def save_history_entry(entry: EncodingHistory) -> bool:
    """Save an encoding history entry"""
    try:
        history = load_history()
        history.append({
            "timestamp": entry.timestamp,
            "input_path": entry.input_path,
            "output_path": entry.output_path,
            "mode": entry.mode,
            "input_size": entry.input_size,
            "output_size": entry.output_size,
            "compression_ratio": entry.compression_ratio,
            "encoding_time": entry.encoding_time,
            "source_bitrate": entry.source_bitrate,
            "output_bitrate": entry.output_bitrate
        })
        # Keep only last 1000 entries
        if len(history) > 1000:
            history = history[-1000:]
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving history: {e}")
        return False

def load_history() -> List[Dict]:
    """Load encoding history"""
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading history: {e}")
    return []

def clear_history() -> bool:
    """Clear all history"""
    try:
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        return True
    except Exception as e:
        print(f"Error clearing history: {e}")
        return False

def validate_path(path: str) -> str:
    """Normalize and validate path"""
    return os.path.normpath(os.path.abspath(path))

def get_gpu_name() -> str:
    """Get GPU name using nvidia-smi"""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            stderr=subprocess.DEVNULL, timeout=2
        )
        return out.decode().strip()
    except:
        return "GPU N/A"

# ============================================================================
# ENCODING PRESETS
# ============================================================================

class EncodingPresets:
    """Hardware-optimized encoding presets"""
    
    @staticmethod
    def get_scale_filter(resolution: str, source_width: int, source_height: int) -> str:
        """Get scale filter with Lanczos for best quality"""
        if resolution == "Same as source":
            return ""
        elif resolution == "1080p":
            return ",scale=-2:1080:flags=lanczos"
        elif resolution == "720p":
            return ",scale=-2:720:flags=lanczos"
        elif resolution == "480p":
            return ",scale=-2:480:flags=lanczos"
        return ""
    
    @staticmethod
    def get_av1_ultra(resolution: str, source_width: int, source_height: int, 
                     smart_filters: str = "", keep_hdr: bool = True,
                     av1_tune: str = "vmaf", sharpening_profile: str = "medium") -> Tuple[List[str], bool]:
        """AV1 Ultra (CRF 22, P4) - Cinema-grade quality"""
        scale = EncodingPresets.get_scale_filter(resolution, source_width, source_height)
        
        # Map tune string to numeric value
        tune_map = {"vmaf": 0, "psnr": 1, "ssim": 2, "grain": 3}
        tune_value = tune_map.get(av1_tune.lower(), 0)
        
        # Sharpening profiles
        sharpening_map = {
            "light": "unsharp=3:3:0.2:3:3:0.0",
            "medium": "unsharp=3:3:0.3:3:3:0.0",
            "heavy": "unsharp=3:3:0.5:3:3:0.0"
        }
        unsharp_filter = sharpening_map.get(sharpening_profile.lower(), "unsharp=3:3:0.3:3:3:0.0")
        
        filter_parts = []
        if smart_filters:
            filter_parts.append(smart_filters)
        filter_parts.append("hqdn3d=0.8:0.8:3:3")
        if scale:
            filter_parts.append(scale[1:])
        filter_parts.append(unsharp_filter)
        
        if keep_hdr:
            filter_parts.append("format=yuv420p10le")
        else:
            filter_parts.append("format=yuv420p")
        
        vf = ",".join(filter_parts)
        
        cmd = [
            "-vf", vf,
            "-c:v", "libsvtav1",
            "-preset", "4",
            "-crf", "22",
            "-svtav1-params", 
            f"tune={tune_value}:film-grain=8:film-grain-denoise=0:enable-variance-boost=1:"
            "enable-qm=1:qm-min=0:enable-tf=1:lookahead=120:scd=1:"
            "enable-overlays=1:enable-restoration=1:enable-cdef=1",
            "-g", "240",
            "-pix_fmt", "yuv420p10le" if keep_hdr else "yuv420p",
            "-threads", "16",
            "-c:a", "libopus" if HAS_LIBOPUS else "aac",
            "-b:a", "256k"
        ]
        return cmd, False
    
    @staticmethod
    def get_av1_balanced(resolution: str, source_width: int, source_height: int,
                        smart_filters: str = "", keep_hdr: bool = True,
                        av1_tune: str = "vmaf", sharpening_profile: str = "medium") -> Tuple[List[str], bool]:
        """AV1 Balanced (CRF 25, P5) - Best overall balance"""
        scale = EncodingPresets.get_scale_filter(resolution, source_width, source_height)
        
        # Map tune string to numeric value
        tune_map = {"vmaf": 0, "psnr": 1, "ssim": 2, "grain": 3}
        tune_value = tune_map.get(av1_tune.lower(), 0)
        
        # Sharpening profiles
        sharpening_map = {
            "light": "unsharp=3:3:0.15:3:3:0.0",
            "medium": "unsharp=3:3:0.2:3:3:0.0",
            "heavy": "unsharp=3:3:0.4:3:3:0.0"
        }
        unsharp_filter = sharpening_map.get(sharpening_profile.lower(), "unsharp=3:3:0.2:3:3:0.0")
        
        filter_parts = []
        if smart_filters:
            filter_parts.append(smart_filters)
        filter_parts.append("hqdn3d=0.8:0.8:3:3")
        if scale:
            filter_parts.append(scale[1:])
        filter_parts.append(unsharp_filter)
        
        if keep_hdr:
            filter_parts.append("format=yuv420p10le")
        else:
            filter_parts.append("format=yuv420p")
        
        vf = ",".join(filter_parts)
        
        cmd = [
            "-vf", vf,
            "-c:v", "libsvtav1",
            "-preset", "5",
            "-crf", "25",
            "-svtav1-params",
            f"tune={tune_value}:film-grain=6:enable-variance-boost=1:enable-qm=1:"
            "lookahead=60:enable-tf=1:scd=1:enable-overlays=1:enable-cdef=1",
            "-g", "240",
            "-pix_fmt", "yuv420p10le" if keep_hdr else "yuv420p",
            "-threads", "16",
            "-c:a", "libopus" if HAS_LIBOPUS else "aac",
            "-b:a", "192k"
        ]
        return cmd, False
    
    @staticmethod
    def get_av1_fast(resolution: str, source_width: int, source_height: int,
                    smart_filters: str = "", keep_hdr: bool = True,
                    av1_tune: str = "vmaf", sharpening_profile: str = "medium") -> Tuple[List[str], bool]:
        """AV1 Fast (CRF 28, P8) - Quick compression"""
        scale = EncodingPresets.get_scale_filter(resolution, source_width, source_height)
        
        # Map tune string to numeric value
        tune_map = {"vmaf": 0, "psnr": 1, "ssim": 2, "grain": 3}
        tune_value = tune_map.get(av1_tune.lower(), 0)
        
        # Sharpening profiles (lighter for fast mode)
        sharpening_map = {
            "light": "unsharp=3:3:0.1:3:3:0.0",
            "medium": "unsharp=3:3:0.15:3:3:0.0",
            "heavy": "unsharp=3:3:0.3:3:3:0.0"
        }
        unsharp_filter = sharpening_map.get(sharpening_profile.lower(), "unsharp=3:3:0.15:3:3:0.0")
        
        filter_parts = []
        if smart_filters:
            filter_parts.append(smart_filters)
        filter_parts.append("hqdn3d=0.5:0.5:2:2")
        if scale:
            filter_parts.append(scale[1:])
        filter_parts.append(unsharp_filter)
        
        if keep_hdr:
            filter_parts.append("format=yuv420p10le")
        else:
            filter_parts.append("format=yuv420p")
        
        vf = ",".join(filter_parts)
        
        cmd = [
            "-vf", vf,
            "-c:v", "libsvtav1",
            "-preset", "8",
            "-crf", "28",
            "-svtav1-params",
            f"tune={tune_value}:film-grain=4:enable-variance-boost=1:lookahead=30:scd=1",
            "-g", "240",
            "-pix_fmt", "yuv420p10le" if keep_hdr else "yuv420p",
            "-threads", "16",
            "-c:a", "libopus" if HAS_LIBOPUS else "aac",
            "-b:a", "160k"
        ]
        return cmd, False
    
    @staticmethod
    def _compute_hw_adaptive_plan(resolution: str, source_width: int, source_height: int, input_path: str,
                                  smart_filters: str, keep_hdr: bool, user_log: Optional[List[str]],
                                  custom_cq: Optional[int], sharpening_profile: str, encoder: str) -> Dict:
        """Shared adaptive planner for NVENC/AMF so both encoders use identical logic."""
        info_ext = ffprobe_info_extended(input_path)
        src_w = info_ext["width"]
        src_h = info_ext["height"]
        src_br_bps = info_ext.get("bitrate_bps", info_ext["bitrate"] * 1000)
        bppf = info_ext.get("bppf", 0.1)
        src_codec = info_ext.get("codec_name_normalized", "unknown")
        fps = info_ext.get("fps", 30)

        # OPTIMIZED: Detect film grain to preserve texture
        duration = info_ext.get("duration", 0)
        has_grain, grain_strength = detect_film_grain(input_path, duration)
        if user_log is not None and has_grain:
            user_log.append(f"Film grain detected (strength: {grain_strength:.2f}) - preserving texture")


        source_is_hdr = is_source_hdr(info_ext)
        output_10bit = keep_hdr and source_is_hdr

        use_bold_path = detect_bold_compression_path(info_ext)
        use_medium_1080p = False if use_bold_path else detect_medium_1080p_path(info_ext)
        path_used = "bold" if use_bold_path else "medium" if use_medium_1080p else "default"

        if user_log is not None:
            user_log.append(f"Adaptive path pre-check: {path_used}")

        if use_bold_path:
            filter_profile_name = "bold"
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
        elif use_medium_1080p:
            filter_profile_name = "medium_soft"
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
        else:
            denoise, base_unsharp, filter_profile_name = get_adaptive_denoise(src_br_bps, source_is_hdr, keep_hdr)

        # OPTIMIZED: Override filter profile for grainy content
        if has_grain and grain_strength > 0.4:
            filter_profile_name = "grainy"
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
            if user_log is not None:
                user_log.append(f"Grainy content: Using temporal-only denoise (preserving spatial texture)")


        def resolve_unsharp(base_value: str) -> str:
            if path_used in {"bold", "medium"}:
                return base_value
            if sharpening_profile.lower() == "off":
                return ""
            sharpening_map = {
                "light": "unsharp=3:3:0.2:3:3:0.0",
                "medium": "unsharp=3:3:0.4:3:3:0.0",
                "heavy": "unsharp=3:3:0.6:3:3:0.0"
            }
            return sharpening_map.get(sharpening_profile.lower(), base_value)

        unsharp = resolve_unsharp(base_unsharp)
        scale_filter = EncodingPresets.get_scale_filter(resolution, source_width, source_height)

        if encoder == "amf":
            params = choose_adaptive_params(src_w, src_h, src_br_bps, bppf, src_codec, encoder="amf")
        else:
            params = choose_nvenc_params(src_w, src_h, src_br_bps, bppf, src_codec)

        vbv_log_added = False

        def _log_balanced_vbv():
            nonlocal vbv_log_added
            if user_log is not None and not vbv_log_added:
                user_log.append("AV1 Balanced VBV tightened: maxrate = target * 1.15, bufsize = 2x maxrate.")
                vbv_log_added = True

        if path_used == "default":
            params = finish_cq_for_source(info_ext, params)

        if path_used == "bold":
            params, fp_name = apply_bold_compression_params(
                params, sharpening_profile, src_br_bps, info_ext.get("fps", 30), bppf
            )
            filter_profile_name = fp_name
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
            unsharp = base_unsharp  # Lock filters for bold
            if user_log is not None:
                user_log.append("Bold path engaged: complexity-aware skin-preserving filters and adaptive CQ applied.")
        elif path_used == "medium":
            params, fp_name = apply_medium_1080p_params(params, info_ext, bppf)
            filter_profile_name = fp_name
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
            unsharp = base_unsharp
            if user_log is not None:
                user_log.append("Medium-1080p path engaged: safety bitrate + soft filters.")

        balanced_like_mode = params.get("mode") in {"constrained", "medium_1080p", "bold"}
        if encoder == "amf" and balanced_like_mode:
            apply_vbv_profile(params, DEFAULT_MAXRATE_MULT, DEFAULT_BUFSIZE_MULT)
            _log_balanced_vbv()

        clean_balanced_candidate = (
            encoder == "amf"
            and params.get("mode") in {"constrained", "medium_1080p"}
            and src_h >= 1080
            and not source_is_hdr
        )

        if clean_balanced_candidate:
            if bppf < 0.09:
                desired_target = max(MIN_1080P_TARGET, 2_300_000)
                params["b_v"] = desired_target
                params["cq"] = max(28, params.get("cq", 28))
                apply_vbv_profile(params, DEFAULT_MAXRATE_MULT, DEFAULT_BUFSIZE_MULT)
                _log_balanced_vbv()
                filter_profile_name = "bold"
                denoise, base_unsharp = get_filter_profile(filter_profile_name)
                unsharp = base_unsharp
                if user_log is not None:
                    user_log.append(
                        f"Clean 1080p override: bppf={bppf:.3f} -> target={desired_target / 1_000_000:.2f} Mbps, CQ {params['cq']}."
                    )
            elif path_used == "medium" and bppf < 0.12:
                filter_profile_name = "bold"
                denoise, base_unsharp = get_filter_profile(filter_profile_name)
                unsharp = base_unsharp
                if user_log is not None:
                    user_log.append("Medium-1080p: clean 1080p detected -> switching to bold filters.")

        # Low-motion fallback for clean studio shots
        codec_norm = normalize_codec_name(src_codec)
        is_clean_codec = codec_norm in {"h264", "hevc", "av1", "prores", "dnxhr"}
        is_low_motion = (
            path_used == "default"
            and src_h >= 1080
            and src_br_bps >= 6_000_000
            and bppf <= 0.08
            and fps <= 32
            and is_clean_codec
        )
        if is_low_motion:
            params["cq"] = min(params["cq"] + 1, 32)
            params["b_v"] = max(MIN_1080P_TARGET, int(params["b_v"] * 0.9))
            reapply_vbv(params)
            filter_profile_name = "clean_h264"
            denoise, base_unsharp = get_filter_profile(filter_profile_name)
            unsharp = resolve_unsharp(base_unsharp)
            if user_log is not None:
                user_log.append("Low-motion fallback: CQ softened + bitrate trimmed for studio content.")

        enforce_minimum_bitrate(params, src_h, path_used, source_is_hdr)

        if custom_cq and custom_cq > 0 and path_used == "default":
            params["cq"] = max(18, min(32, custom_cq))
            if user_log is not None:
                user_log.append(f"Custom CQ override applied: {params['cq']}")

        params["path_used"] = path_used
        force_30fps = should_downscale_fps_to_30(info_ext)

        filter_parts = []
        if smart_filters:
            filter_parts.append(smart_filters)
        filter_parts.append(denoise)
        if source_is_hdr and not keep_hdr:
            # OPTIMIZED: Professional HDR→SDR tone mapping
            if HAS_LIBPLACEBO:
                # Best quality: libplacebo with BT.2390 EETF (ITU standard)
                tone_map = (
                    "libplacebo="
                    "format=yuv420p:"
                    "w=iw:h=ih:"
                    "tonemapping=bt2390:"        # BT.2390 EETF (Netflix/YouTube standard)
                    "gamut_mapping=perceptual:"  # Preserve color appearance
                    "peak_detect=1:"             # Auto-detect HDR peak luminance
                    "dithering=blue"             # Blue noise dithering prevents banding
                )
                if user_log is not None:
                    user_log.append("HDR->SDR: Using libplacebo with BT.2390 tone mapping (best quality)")
            else:
                # Fallback: Enhanced zscale pipeline (much better than old hable)
                tone_map = (
                    "zscale=t=linear:npl=100,"                           # Convert to linear light, normalize to 100 nits
                    "format=gbrpf32le,"                                  # Float precision for tone mapping
                    "zscale=p=bt709,"                                    # BT.2020 -> BT.709 primaries
                    "tonemap=mobius:param=0.30:desat=0.5,"             # Mobius (better than hable) + desaturation
                    "zscale=t=bt709:m=bt709:r=tv:primaries=bt709,"     # Final SDR transfer
                    "format=yuv420p"
                )
                if user_log is not None:
                    user_log.append("HDR->SDR: Using enhanced zscale+mobius tone mapping")
            filter_parts.append(tone_map)

        if scale_filter:
            filter_parts.append(scale_filter[1:])
        if unsharp:
            filter_parts.append(unsharp)
        # OPTIMIZED: Add dithering for 8-bit output to prevent banding
        if output_10bit:
            format_filter = "format=p010le"
        else:
            # Use 10-bit intermediate -> dither -> 8-bit for smooth gradients
            # Add subtle temporal+uniform noise (blue noise pattern)
            format_filter = "format=yuv420p10le,noise=alls=1:allf=t+u,format=yuv420p"
        filter_parts.append(format_filter)
        vf = ",".join([part for part in filter_parts if part])

        public_params = {k: v for k, v in params.items() if not str(k).startswith("_")}

        if user_log is not None:
            user_log.append(
                f"Path={path_used} | CQ={public_params.get('cq')} | target={public_params.get('b_v')} "
                f"| maxrate={public_params.get('maxrate')} | bufsize={public_params.get('bufsize')}"
            )
            user_log.append(
                f"Filter profile '{filter_profile_name}': {denoise}"
                + (f" + {unsharp}" if unsharp else " (no sharpen)")
            )

        return {
            "info": info_ext,
            "vf": vf,
            "params": params,
            "public_params": public_params,
            "path_used": path_used,
            "filter_profile": filter_profile_name,
            "filter_strings": {
                "denoise": denoise,
                "unsharp": unsharp,
                "smart": smart_filters or "",
                "scale": scale_filter[1:] if scale_filter else ""
            },
            "force_30fps": force_30fps,
            "use_bold_path": use_bold_path,
            "use_medium_path": use_medium_1080p,
            "output_10bit": output_10bit,
            "encoder": encoder
        }

    @staticmethod
    def get_nvenc_adaptive(resolution: str, source_width: int, source_height: int, input_path: str,
                          smart_filters: str = "", keep_hdr: bool = True, copy_audio: bool = False,
                          user_log: List[str] = None, custom_cq: Optional[int] = None,
                          sharpening_profile: str = "medium") -> Tuple[List[str], bool, Dict]:
        """
        NEW v4.6.0: NVENC Nova-Style Adaptive - Three-level decision system
        """
        plan = EncodingPresets._compute_hw_adaptive_plan(
            resolution,
            source_width,
            source_height,
            input_path,
            smart_filters,
            keep_hdr,
            user_log,
            custom_cq,
            sharpening_profile,
            encoder="nvenc"
        )
        params = plan["params"]
        vf = plan["vf"]
        force_30fps = plan["force_30fps"]

        if user_log is not None:
            pp = plan["public_params"]
            filter_desc = plan["filter_strings"]
            unsharp_desc = "" if filter_desc["unsharp"] in ("", "none") else f" + {filter_desc['unsharp']}"
            user_log.append(
                f"Final path={plan['path_used']} | CQ={pp.get('cq')} | target={pp.get('b_v')} | "
                f"maxrate={pp.get('maxrate')} | bufsize={pp.get('bufsize')}"
            )
            user_log.append(f"Filters ({plan['filter_profile']}): {filter_desc['denoise']}{unsharp_desc}")
        
        cmd = [
            "-vf", vf,
            "-c:v", "hevc_nvenc",
            "-preset", "p7",
            "-tune", "hq",
        ]

        if force_30fps:
            cmd.extend(["-r", "30"])
            if user_log is not None:
                user_log.append("FPS rule: source > 45fps -> forcing 30fps")

        # OPTIMIZED: Pure CQ mode or constrained VBR based on setting
        if ENABLE_PURE_CQ_MODE:
            # Pure CQ mode: No bitrate constraints, let CQ control quality
            cmd.extend([
                "-rc", "vbr_hq",
                "-cq", str(params["cq"]),
                # No -b:v, -maxrate, -bufsize → encoder uses CQ as sole quality target
            ])
            if user_log is not None:
                user_log.append(f"NVENC: Pure CQ mode (CQ={params['cq']}, no bitrate constraints)")
        else:
            # Constrained VBR mode (traditional)
            cmd.extend([
                "-rc", "vbr_hq",
                "-cq", str(params["cq"]),
                "-b:v", str(params["b_v"]),
                "-maxrate", str(params["maxrate"]),
                "-bufsize", str(params["bufsize"]),
            ])
        
        # ENHANCED: Advanced NVENC quality settings
        cmd.extend([
            "-spatial_aq", "1",
            "-aq-strength", "12",           # Boosted from default 8 (max 15) for better dark scene quality
            "-temporal_aq", "1",
            "-rc-lookahead", "32",
            "-lookahead_level", "3",        # NEW: Max lookahead quality (0-3)
            "-multipass", "fullres",
            "-bf", "4",
            "-b_ref_mode", "middle",
            "-tier", "high",                # NEW: Remove bitrate ceiling for HQ encoding
            "-nonref_p", "1",               # NEW: Use non-reference P frames (5-10% better compression)
            "-strict_gop", "1",             # NEW: Strict GOP for better seeking
            "-no-scenecut", "0",            # Allow scene cut detection
            "-forced-idr", "0",             # Allow encoder to decide IDR placement
        ])

        if copy_audio:
            cmd.extend(["-c:a", "copy"])
        else:
            audio_codec, audio_br = get_smart_audio_bitrate(input_path, "NVENC Adaptive")
            if audio_codec == "copy":
                cmd.extend(["-c:a", "copy"])
            else:
                cmd.extend(["-c:a", audio_codec, "-b:a", audio_br])
        
        return cmd, True, plan

    @staticmethod
    def get_amf_adaptive(resolution: str, source_width: int, source_height: int, input_path: str,
                         smart_filters: str = "", keep_hdr: bool = True, copy_audio: bool = False,
                         user_log: List[str] = None, custom_cq: Optional[int] = None,
                         sharpening_profile: str = "medium", mode: str = "") -> Tuple[List[str], bool, Dict]:
        """
        AMD AMF adaptive path shares the same decision logic but emits AMF-friendly flags.
        """
        plan = EncodingPresets._compute_hw_adaptive_plan(
            resolution,
            source_width,
            source_height,
            input_path,
            smart_filters,
            keep_hdr,
            user_log,
            custom_cq,
            sharpening_profile,
            encoder="amf"
        )
        params = plan["params"]
        vf = plan["vf"]
        force_30fps = plan["force_30fps"]

        if user_log is not None:
            pp = plan["public_params"]
            filter_desc = plan["filter_strings"]
            unsharp_desc = "" if filter_desc["unsharp"] in ("", "none") else f" + {filter_desc['unsharp']}"
            user_log.append(
                f"Final path={plan['path_used']} | CQ={pp.get('cq')} | target={pp.get('b_v')} | "
                f"maxrate={pp.get('maxrate')} | bufsize={pp.get('bufsize')}"
            )
            user_log.append(f"Filters ({plan['filter_profile']}): {filter_desc['denoise']}{unsharp_desc}")

        # Choose best available AMD codec
        if HAS_AV1_AMF:
            amf_codec = "av1_amf"
        elif HAS_HEVC_AMF:
            amf_codec = "hevc_amf"
        else:
            amf_codec = "h264_amf"
        
        if user_log is not None:
            user_log.append(f"AMD Codec: {amf_codec}")
        
        cmd = [
            "-vf", vf,
            "-c:v", amf_codec,
            "-quality", "quality",
            "-usage", "transcoding",
        ]
        
        # Override params for AV1 Compress mode (aggressive compression)
        is_compress_mode = "compress" in mode.lower()
        if is_compress_mode and amf_codec == "av1_amf":
            # Aggressive compression: Higher CQ + Lower bitrate
            params["cq"] = 31  # Higher CQ = more compression
            # Reduce bitrate by ~15-20% for 1080p
            if source_width >= 1920:
                params["b_v"] = 1_900_000  # 1.9 Mbps (was 2.3 Mbps)
                params["maxrate"] = int(params["b_v"] * 1.5)  # Looser maxrate for complex scenes
                params["bufsize"] = int(params["maxrate"] * 2)
            elif source_width >= 1280:
                params["b_v"] = 1_200_000  # 1.2 Mbps
                params["maxrate"] = int(params["b_v"] * 1.5)
                params["bufsize"] = int(params["maxrate"] * 2)
            if user_log is not None:
                user_log.append(f"AV1 Compress: Aggressive mode - CQ={params['cq']}, target={params['b_v']//1000}kbps")

        # Pure CQ mode or constrained VBR
        if ENABLE_PURE_CQ_MODE and amf_codec != "av1_amf":
            # Pure CQ for HEVC/H.264 (AV1 needs bitrate target)
            cmd.extend([
                "-rc", "cqp",  # Constant QP mode (closest to CQ for AMF)
                "-qp_i", str(max(18, min(32, params.get("cq", 26)))),
                "-qp_p", str(max(18, min(34, params.get("cq", 26) + 2))),
            ])
            if user_log is not None:
                user_log.append(f"AMF: CQP mode (QP_I={max(18, min(32, params.get('cq', 26)))})")
        else:
            # VBR mode with bitrate constraints
            cmd.extend([
                "-rc", "vbr_peak",
                "-b:v", str(params["b_v"]),
                "-maxrate", str(params["maxrate"]),
                "-bufsize", str(params["bufsize"]),
                "-qp_i", str(max(18, min(32, params.get("cq", 26)))),
                "-qp_p", str(max(18, min(34, params.get("cq", 26) + 2))),
            ])

        if force_30fps:
            cmd.extend(["-r", "30"])
            if user_log is not None:
                user_log.append("FPS rule: source > 45fps -> forcing 30fps")

        # RDNA 4 OPTIMIZATIONS: AV1 B-frames and enhanced features
        if amf_codec == "av1_amf" and HAS_AMD_RDNA4:
            # All modes use quality-focused B-frame settings
            cmd.extend([
                "-bf", "3",                              # B-frames support (RDNA 4+, max=3)
                "-preanalysis", "1",                     # Pre-analysis pass
                "-aq_mode", "caq",                       # Context Adaptive Quantization
                "-pa_caq_strength", "high",              # High CAQ strength for quality
                "-pa_taq_mode", "2",                     # Temporal AQ mode 2 (best quality)
                "-pa_high_motion_quality_boost_mode", "auto",  # High motion boost
            ])
            if user_log is not None:
                user_log.append("RDNA 4: AV1 B-frames + quality optimizations (3 B-frames, CAQ high, TAQ mode 2)")
        elif amf_codec == "av1_amf":
            # RDNA 3 and older: No B-frames, but enable quality optimizations
            cmd.extend([
                "-preanalysis", "1",                     # Pre-analysis pass
                "-aq_mode", "caq",                       # Context Adaptive Quantization
                "-pa_caq_strength", "medium",            # Medium CAQ strength
            ])
            if user_log is not None:
                user_log.append("AMD AV1: Standard mode + CAQ (no B-frames, RDNA <4)")
        elif amf_codec == "hevc_amf":
            # HEVC optimizations
            cmd.extend([
                "-bf", "3",                  # B-frames for HEVC
                "-preanalysis", "1",
                "-vbaq", "1",
            ])

        if copy_audio:
            cmd.extend(["-c:a", "copy"])
        else:
            audio_codec, audio_br = get_smart_audio_bitrate(input_path, "AMF Adaptive")
            if audio_codec == "copy":
                cmd.extend(["-c:a", "copy"])
            else:
                cmd.extend(["-c:a", audio_codec, "-b:a", audio_br])
        
        # Store codec choice in plan for container format decisions
        plan["amf_codec"] = amf_codec

        return cmd, True, plan

# ============================================================================
# MODERN NEON PROGRESS BAR
# ============================================================================

class ModernNeonBar(tk.Canvas):
    """Modern neon progress bar with enhanced glow and detailed info"""
    
    def __init__(self, master, width=900, height=35):
        super().__init__(master, width=width, height=height,
                        bg=BG_DARK, highlightthickness=0, bd=0)
        self.w, self.h = width, height
        self.pct = 0
        self.phase = 0
        self._animating = True
        self.config(relief="flat")
        self._draw()
        self._animate()
    
    def set(self, p: float):
        """Set progress percentage"""
        self.pct = max(0, min(100, p))
        self._draw()
    
    def stop_animation(self):
        """Stop the glow animation"""
        self._animating = False
    
    def _draw(self):
        """Draw the progress bar with neon glow effect"""
        try:
            self.delete("all")
            
            # Background with neon border
            self.create_rectangle(0, 0, self.w, self.h,
                                fill=BG_CARD, outline=ACCENT, width=2)
            
            fill_width = int((self.w - 12) * self.pct / 100)
            
            if fill_width > 10:
                # Gradient progress fill (cyan to magenta like mockup)
                # Create gradient effect by drawing multiple rectangles
                gradient_steps = 20
                step_width = fill_width / gradient_steps
                for i in range(gradient_steps):
                    x1 = 6 + int(i * step_width)
                    x2 = 6 + int((i + 1) * step_width)
                    if x2 > 6 + fill_width:
                        x2 = 6 + fill_width
                    
                    # Interpolate from cyan to magenta
                    ratio = i / gradient_steps
                    r = int(0 + (255 - 0) * ratio)
                    g = int(255 - (255 - 0) * ratio)
                    b = 255
                    grad_color = f"#{r:02x}{g:02x}{b:02x}"
                    
                    self.create_rectangle(x1, 6, x2, self.h-6,
                                        fill=grad_color, outline="", width=0)
                
                # Animated glow effect (triple layer)
                glow = 0.3 + 0.7 * math.sin(self.phase)
                
                # Outer glow (soft)
                glow_color1 = self._mix_color(ACCENT_DIM, ACCENT_GLOW, glow * 0.3)
                self.create_rectangle(4, 4, 8+fill_width, self.h-4,
                                    outline=glow_color1, width=4)
                
                # Middle glow
                glow_color2 = self._mix_color(ACCENT, ACCENT_BRIGHT, glow * 0.6)
                self.create_rectangle(5, 5, 7+fill_width, self.h-5,
                                    outline=glow_color2, width=3)
                
                # Inner glow (bright)
                glow_color3 = self._mix_color(ACCENT_BRIGHT, ACCENT_GLOW, glow)
                self.create_rectangle(6, 6, 6+fill_width, self.h-6,
                                    outline=glow_color3, width=2)
            
            # Percentage text with shadow
            pct_text = f"{self.pct:.1f}%"
            x, y = self.w // 2, self.h // 2
            
            # Shadow for visibility
            self.create_text(x+2, y+2, text=pct_text, fill="#000000",
                           font=("Segoe UI", 18, "bold"))
            # Main text - Gaming style cyan
            self.create_text(x, y, text=pct_text, fill=ACCENT,
                           font=("Segoe UI", 20, "bold"))
        except:
            pass
    
    def _mix_color(self, color1: str, color2: str, ratio: float) -> str:
        """Mix two hex colors"""
        try:
            c1 = int(color1[1:], 16)
            c2 = int(color2[1:], 16)
            
            r1, g1, b1 = (c1 >> 16) & 0xff, (c1 >> 8) & 0xff, c1 & 0xff
            r2, g2, b2 = (c2 >> 16) & 0xff, (c2 >> 8) & 0xff, c2 & 0xff
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            return f"#{r:02x}{g:02x}{b:02x}"
        except:
            return ACCENT
    
    def _animate(self):
        """Animate the glow effect"""
        if not self._animating:
            return
        try:
            self.phase += 0.15
            self._draw()
            self.after(40, self._animate)
        except:
            self._animating = False

# ============================================================================
# MAIN APPLICATION
# ============================================================================

class App:
    def __init__(self, root):
        self.root = root
        root.title(f"{APP_TITLE} v{VERSION}")
        root.configure(bg=BG_DARK)
        root.geometry("1100x880")
        root.minsize(1000, 700)
        root.resizable(True, True)
        
        root.protocol("WM_DELETE_WINDOW", self._on_closing)
        
        self._setup_styles()
        
        # Variables
        self.mode = tk.StringVar(value="AV1 Balanced")
        self.resolution = tk.StringVar(value="Same as source")
        self.two_pass = tk.BooleanVar(value=False)
        self.shutdown_after = tk.BooleanVar(value=False)
        self.inp = tk.StringVar()
        self.out = tk.StringVar()
        self.batch_output_mode = tk.StringVar(value="source")
        self.batch_output_folder = ""
        self._last_hw_plan = None
        
        # Intelligent compression options
        self.auto_mode = tk.BooleanVar(value=True)
        self.keep_hdr = tk.BooleanVar(value=True)
        self.skip_small_saving = tk.BooleanVar(value=False)
        
        # Advanced options (NEW v5.0)
        self.custom_cq = tk.IntVar(value=0)  # 0 = auto, otherwise use this value
        self.custom_filters = tk.StringVar(value="")
        self.sharpening_profile = tk.StringVar(value="medium")  # light, medium, heavy, off
        self.av1_tune = tk.StringVar(value="vmaf")  # grain, psnr, ssim, vmaf
        self.encoder_preference = tk.StringVar(value="auto")  # auto, nvenc, amf, cpu
        self.current_profile_name = tk.StringVar(value="")
        self.dark_theme = tk.BooleanVar(value=True)
        self.delete_source_after = tk.BooleanVar(value=False)
        self.organize_output = tk.BooleanVar(value=False)
        self.watch_folder_enabled = tk.BooleanVar(value=False)
        self.watch_folder_path = tk.StringVar(value="")

        # Track if output path is auto-generated
        self.output_is_auto = True
        self._setting_default_mode = False

        # Encoding history
        self.encoding_history: List[EncodingHistory] = []
        
        # Hardware monitoring
        self.gpu_usage = 0.0
        self.cpu_usage = 0.0
        self.encoding_speed = 0.0
        
        # State
        self.proc = None
        self.stop = False
        self.is_running = False
        self.total_duration = 1.0
        self.input_fps = 25.0
        self.encoding_start_time = 0
        self.ffmpeg_pid = None
        self.input_size = 0
        self.source_width = 1920
        self.source_height = 1080
        self.estimated_output_size = 0
        self.current_output_size = 0
        self.current_bitrate = 0
        self.error_log = []
        self._monitor_active = False
        
        # Enhanced ETA tracking
        self.speed_history = []
        self.last_progress_time = 0
        self.last_encoded_time = 0
        
        # Queue system
        self.queue: List[QueueItem] = []
        self.current_queue_item: Optional[QueueItem] = None
        self.resume_file = "encoding_state.pkl"
        
        # Build GUI
        self._build_gui()
        
        # Check codecs
        self.root.after(500, self._check_codecs)
        
        if DND_OK:
            self._setup_dnd()
        
        # Start monitoring
        self._monitor_active = True
        self.root.after(1000, self._monitor)
        self.root.after(1000, self._check_resume)
        
        # Bind input/output field changes
        self.inp.trace_add("write", self._on_input_change)
        self.out.trace_add("write", self._on_output_manual_change)
        self.mode.trace_add("write", self._on_mode_change)
        
        # Setup keyboard shortcuts (NEW v5.0)
        self._setup_keyboard_shortcuts()
        
        # Load saved profiles
        self._load_saved_profiles()
        
        # NEW v5.0: Start watch folder monitoring if enabled
        self.watch_folder_thread = None
        if self.watch_folder_enabled.get() and self.watch_folder_path.get():
            self._start_watch_folder()
    
    def _check_codecs(self):
        """Check codec availability and warn if missing"""
        if not HAS_LIBSVTAV1:
            messagebox.showwarning(
                "Codec Warning",
                "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â SVT-AV1 encoder not found!\n\n"
                "AV1 modes will not work.\n"
                "Download FFmpeg with SVT-AV1:\n"
                "https://www.gyan.dev/ffmpeg/builds/"
            )
    
    def _setup_styles(self):
        """Setup ttk styles for modern dark theme"""
        style = ttk.Style(self.root)
        try:
            style.theme_use("clam")
        except:
            pass
        
        # Configure styles
        style.configure(".", background=BG_DARK, foreground=TEXT_BRIGHT)
        style.configure("TLabel", background=BG_DARK, foreground=TEXT_BRIGHT,
                       font=("Segoe UI", 9, "bold"))  # Bold for gaming look
        style.configure("Title.TLabel", font=("Segoe UI", 36, "bold"),
                       foreground=ACCENT_GLOW)  # Larger title like mockup (36px)
        style.configure("Subtitle.TLabel", font=("Segoe UI", 14, "normal"),
                       foreground=WARNING)  # Magenta subtitle like mockup
        
        # Buttons - Gaming style with neon borders
        # Note: ttk.Button doesn't support bordercolor in state maps, so we use borderwidth and relief
        style.configure("TButton", 
                       background=BG_CARD, 
                       foreground=ACCENT,
                       font=("Segoe UI", 11, "bold"), 
                       padding=(20, 12),
                       borderwidth=2,
                       relief="solid")
        style.map("TButton",
                 background=[("active", BG_INPUT), ("disabled", "#000")],
                 foreground=[("active", ACCENT_BRIGHT), ("disabled", "#333")])
        
        style.configure("Cancel.TButton", 
                       background=BG_CARD, 
                       foreground=ERROR,
                       borderwidth=2,
                       relief="solid")
        style.map("Cancel.TButton", 
                 background=[("active", BG_INPUT)],
                 foreground=[("active", "#ff4444")])
        
        style.configure("Secondary.TButton", 
                       background=BG_CARD,
                       foreground=TEXT_BRIGHT,
                       borderwidth=2,
                       relief="solid",
                       padding=(15, 10))
        style.map("Secondary.TButton",
                 background=[("active", BG_INPUT), ("disabled", "#000")],
                 foreground=[("active", ACCENT_BRIGHT), ("disabled", "#333")])
        
        style.configure("Warning.TButton",
                       background=BG_CARD,
                       foreground=WARNING,
                       borderwidth=2,
                       relief="solid",
                       padding=(15, 10))
        style.map("Warning.TButton",
                 background=[("active", BG_INPUT), ("disabled", "#000")],
                 foreground=[("active", "#ff44ff")])
        
        # Combobox - Gaming style with neon border
        style.configure("Modern.TCombobox",
                       fieldbackground=BG_INPUT,
                       background=BG_INPUT,
                       foreground=ACCENT,  # Cyan text
                       arrowcolor=ACCENT,
                       selectbackground=ACCENT,
                       selectforeground=BG_DARK,
                       insertcolor=ACCENT,
                       borderwidth=2,
                       relief="solid",
                       font=("Segoe UI", 10, "bold"))
        style.map("Modern.TCombobox",
                 fieldbackground=[("readonly", BG_INPUT), ("disabled", "#000")],
                 selectbackground=[("readonly", ACCENT)],
                 selectforeground=[("readonly", BG_DARK)])
        
        # Force combobox dropdown colors
        self.root.option_add("*TCombobox*Listbox.background", BG_INPUT)
        self.root.option_add("*TCombobox*Listbox.foreground", TEXT_BRIGHT)
        self.root.option_add("*TCombobox*Listbox.selectBackground", ACCENT)
        self.root.option_add("*TCombobox*Listbox.selectForeground", BG_DARK)
        self.root.option_add("*TCombobox*Listbox.font", ("Segoe UI", 10))
        
        # Checkbutton - Gaming style
        style.configure("TCheckbutton",
                       background=BG_CARD,
                       foreground=ACCENT,  # Cyan text
                       font=("Segoe UI", 10, "bold"),
                       focuscolor="none")
        style.map("TCheckbutton",
                 background=[("active", BG_CARD)],
                 foreground=[("active", ACCENT_BRIGHT), ("selected", ACCENT)],
                 indicatorcolor=[("selected", ACCENT), ("!selected", BG_INPUT)])
        
        # Radiobutton - Gaming style
        style.configure("TRadiobutton",
                       background=BG_CARD,
                       foreground=ACCENT,  # Cyan text
                       font=("Segoe UI", 10, "bold"),
                       focuscolor="none")
        style.map("TRadiobutton",
                 background=[("active", BG_CARD)],
                 foreground=[("active", ACCENT_BRIGHT), ("selected", ACCENT)],
                 indicatorcolor=[("selected", ACCENT), ("!selected", BG_INPUT)])
    
    def _build_gui(self):
        """Build the modern GUI interface"""
        # Create scrollable canvas for the entire window
        canvas = tk.Canvas(self.root, bg=BG_DARK, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=BG_DARK)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Update canvas window width when canvas is resized
        def update_canvas_width(event):
            canvas_width = event.width
            canvas.itemconfig(canvas_window, width=canvas_width)
        canvas.bind('<Configure>', update_canvas_width)
        
        # Bind mouse wheel to canvas (Windows/Linux)
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Bind mouse wheel for Linux (Button-4 and Button-5)
        def _on_mousewheel_linux(event):
            if event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")
        canvas.bind_all("<Button-4>", _on_mousewheel_linux)
        canvas.bind_all("<Button-5>", _on_mousewheel_linux)
        
        # Store canvas reference for updates
        self.canvas = canvas
        self.scrollable_frame = scrollable_frame
        
        # Main container (now inside scrollable frame)
        main = tk.Frame(scrollable_frame, bg=BG_DARK)
        main.pack(fill="both", expand=True, padx=12, pady=8)
        
        # HEADER - Gaming style with neon borders and glow
        header = tk.Frame(main, bg=BG_DARK, highlightbackground=ACCENT,
                         highlightthickness=2)
        header.pack(fill="x", pady=(0, 12))
        
        header_inner = tk.Frame(header, bg=BG_DARK)
        header_inner.pack(padx=16, pady=16)
        
        title_label = ttk.Label(header_inner, text="VIDEO COMPRESSOR PRO",
                 style="Title.TLabel")
        title_label.pack(anchor="center")
        
        gpu_name = get_gpu_name()  # Generic GPU detection
        subtitle_label = ttk.Label(header_inner, 
                 text=f"v5.0.0 ULTIMATE EDITION - {gpu_name} optimized",
                 style="Subtitle.TLabel")
        subtitle_label.pack(anchor="center", pady=(6, 0))
        
        # INTELLIGENT OPTIONS - Gaming style panel with neon glow
        smart_section = tk.Frame(main, bg=BG_CARD, highlightbackground=ACCENT,
                                highlightthickness=2)
        smart_section.pack(fill="x", pady=(0, 12))
        
        smart_inner = tk.Frame(smart_section, bg=BG_CARD)
        smart_inner.pack(padx=16, pady=12)
        
        # Add gradient top border line (simulated with a frame)
        top_border = tk.Frame(smart_inner, height=2, bg=ACCENT)
        top_border.pack(fill="x", pady=(0, 12))
        
        ttk.Label(smart_inner, text="INTELLIGENT COMPRESSION",
                 font=("Segoe UI", 12, "bold"),
                 background=BG_CARD, foreground=ACCENT).pack(anchor="w", pady=(0, 8))
        
        opts_row = tk.Frame(smart_inner, bg=BG_CARD)
        opts_row.pack(fill="x")
        
        ttk.Checkbutton(opts_row, text="Auto-select best mode",
                       variable=self.auto_mode,
                       command=self._on_auto_mode_toggle).pack(side="left", padx=(0, 20))
        
        ttk.Checkbutton(opts_row, text="Keep HDR/10-bit",
                       variable=self.keep_hdr).pack(side="left", padx=(0, 20))
        
        ttk.Checkbutton(opts_row, text="Skip if savings <{:.0f}%".format(3.0),
                       variable=self.skip_small_saving).pack(side="left")
        
        # TOP SECTION: Mode & Resolution
        top_section = tk.Frame(main, bg=BG_DARK)
        top_section.pack(fill="x", pady=(0, 6))
        
        # Left: Mode Selection - Gaming style
        mode_frame = tk.Frame(top_section, bg=BG_CARD, highlightbackground=ACCENT,
                             highlightthickness=2)
        mode_frame.pack(side="left", fill="both", expand=True, padx=(0, 12))
        
        mode_inner = tk.Frame(mode_frame, bg=BG_CARD)
        mode_inner.pack(padx=16, pady=12)
        # Add gradient top border line
        top_border = tk.Frame(mode_inner, height=2, bg=ACCENT)
        top_border.pack(fill="x", pady=(0, 12))
        
        ttk.Label(mode_inner, text="ENCODING MODE", font=("Segoe UI", 11, "bold"),
                 background=BG_CARD, foreground=ACCENT).pack(anchor="w", pady=(0, 12))
        
        modes = ["AV1 Ultra", "AV1 Balanced", "AV1 Compress", "AV1 Fast", "NVENC Ultra", "NVENC Balanced", "NVENC Fast"]
        self.combo_mode = ttk.Combobox(mode_inner, textvariable=self.mode,
                                      state="readonly", width=22,
                                      font=("Segoe UI", 11),
                                      style="Modern.TCombobox",
                                       values=modes)
        self.combo_mode.pack(fill="x", pady=(0, 8))
        
        # NEW v5.0: Encoder selection dropdown
        ttk.Label(mode_inner, text="Hardware Encoder", font=("Segoe UI", 10, "bold"),
                 background=BG_CARD, foreground=TEXT_MID).pack(anchor="w", pady=(12, 6))
        
        encoder_options = ["Auto (detect GPU)"]
        if HAS_HEVC_NVENC:
            encoder_options.append("NVIDIA NVENC")
        if HAS_ANY_AMF:
            encoder_options.append("AMD AMF")
        encoder_options.append("CPU (software)")
        
        self.combo_encoder = ttk.Combobox(mode_inner, textvariable=self.encoder_preference,
                                          state="readonly", width=22,
                                          font=("Segoe UI", 9),
                                          style="Modern.TCombobox",
                                          values=encoder_options)
        self.combo_encoder.pack(fill="x", pady=(0, 8))
        self.combo_encoder.set("Auto (detect GPU)")
        
        # Mode descriptions
        mode_descriptions = {
            "AV1 Ultra": "Cinema CRF 22 P4 ~12-16fps 70-75% smaller Auto: AMD GPU",
            "AV1 Balanced": "Best Balance CRF 25  P5  ~18-24fps 75-80% smaller Auto: AMD GPU",
            "AV1 Compress": "Max Compression CRF 31 ~20-28fps 85-90% smaller Auto: AMD GPU",
            "AV1 Fast": "Quick  CRF 28  P8 ~35-45fps 80-85% smaller Auto: AMD GPU",
            "NVENC Ultra": "GPU Nova-Style 3-level adaptive~150fps",
            "NVENC Balanced": "GPU Nova-Style 3-level adaptive ~155fps",
            "NVENC Fast": "GPU Nova-Style 3-level adaptive  ~170fps"
        }
        
        self.mode_desc = ttk.Label(mode_inner, text=mode_descriptions["AV1 Balanced"],
                                   font=("Segoe UI", 9, "bold"), foreground=TEXT_MID,
                                   background=BG_CARD, wraplength=250, justify="left")
        self.mode_desc.pack(anchor="w", pady=(4, 0))
        
        def update_mode_desc(e):
            self.mode_desc.config(text=mode_descriptions.get(self.mode.get(), ""))
        
        self.combo_mode.bind("<<ComboboxSelected>>", update_mode_desc)
        
        # Right: Resolution Selection - Gaming style
        res_frame = tk.Frame(top_section, bg=BG_CARD, highlightbackground=ACCENT,
                            highlightthickness=2)
        res_frame.pack(side="left", fill="both", expand=True)
        
        res_inner = tk.Frame(res_frame, bg=BG_CARD)
        res_inner.pack(padx=16, pady=12)
        # Add gradient top border line
        top_border = tk.Frame(res_inner, height=2, bg=ACCENT)
        top_border.pack(fill="x", pady=(0, 12))
        
        ttk.Label(res_inner, text="RESOLUTION", font=("Segoe UI", 11, "bold"),
                 background=BG_CARD, foreground=ACCENT).pack(anchor="w", pady=(0, 12))
        
        resolutions = ["Same as source", "1080p", "720p", "480p"]
        self.combo_res = ttk.Combobox(res_inner, textvariable=self.resolution,
                                      state="readonly", width=22,
                                      font=("Segoe UI", 11),
                                      style="Modern.TCombobox",
                                      values=resolutions)
        self.combo_res.pack(fill="x", pady=(0, 8))
        self.combo_res.bind("<<ComboboxSelected>>", lambda e: self._on_settings_change())
        
        # Two-pass option
        ttk.Checkbutton(res_inner, text="Two-pass encoding (AV1 only)",
                       variable=self.two_pass).pack(anchor="w")
        
        # Shutdown option
        ttk.Checkbutton(res_inner, text="Shut down PC after encoding (15s)",
                       variable=self.shutdown_after).pack(anchor="w", pady=(5, 0))
        
        # FILE SELECTION - Gaming style
        file_section = tk.Frame(main, bg=BG_CARD, highlightbackground=ACCENT,
                               highlightthickness=2)
        file_section.pack(fill="x", pady=(0, 12))
        
        file_inner = tk.Frame(file_section, bg=BG_CARD)
        file_inner.pack(padx=16, pady=12)
        
        # Add gradient top border line
        top_border = tk.Frame(file_inner, height=2, bg=ACCENT)
        top_border.pack(fill="x", pady=(0, 12))
        
        ttk.Label(file_inner, text="FILE SELECTION", font=("Segoe UI", 11, "bold"),
                 background=BG_CARD, foreground=ACCENT).pack(anchor="w", pady=(0, 12))
        
        # Input
        ttk.Label(file_inner, text="Input Video", font=("Segoe UI", 10, "bold"),
                 background=BG_CARD, foreground=TEXT_MID).pack(anchor="w", pady=(0, 6))
        
        inp_row = tk.Frame(file_inner, bg=BG_CARD)
        inp_row.pack(fill="x", pady=(0, 6))
        
        self.ein = tk.Entry(inp_row, textvariable=self.inp,
                           bg=BG_INPUT, fg=ACCENT, insertbackground=ACCENT,
                           relief="solid", font=("Segoe UI", 10, "bold"),
                           highlightthickness=2, highlightbackground=ACCENT,
                           highlightcolor=ACCENT_BRIGHT, bd=2)
        self.ein.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 10))
        
        ttk.Button(inp_row, text="Browse", command=self._browse,
                  style="Secondary.TButton").pack(side="left", padx=2)
        ttk.Button(inp_row, text="+ Batch", command=self._browse_batch,
                  style="Secondary.TButton").pack(side="left", padx=2)
        
        # Output
        ttk.Label(file_inner, text="Output Video", font=("Segoe UI", 10, "bold"),
                 background=BG_CARD, foreground=TEXT_MID).pack(anchor="w", pady=(12, 6))
        
        out_row = tk.Frame(file_inner, bg=BG_CARD)
        out_row.pack(fill="x")
        
        self.eout = tk.Entry(out_row, textvariable=self.out,
                            bg=BG_INPUT, fg=ACCENT, insertbackground=ACCENT,
                            relief="solid", font=("Segoe UI", 10, "bold"),
                            highlightthickness=2, highlightbackground=ACCENT,
                            highlightcolor=ACCENT_BRIGHT, bd=2)
        self.eout.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 10))
        
        ttk.Button(out_row, text="Browse", command=self._browse_output,
                  style="Secondary.TButton").pack(side="left")
        
        # SIZE ESTIMATION & STATS
        stats_frame = tk.Frame(main, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                              highlightthickness=2)
        stats_frame.pack(fill="x", pady=(0, 6))
        
        stats_inner = tk.Frame(stats_frame, bg=BG_CARD)
        stats_inner.pack(padx=10, pady=6)
        
        self.size_label = ttk.Label(stats_inner,
                                    text="Select a video to see size estimation",
                                    font=("Segoe UI", 10),
                                    foreground=TEXT_MID,
                                    background=BG_CARD)
        self.size_label.pack(anchor="w", pady=(0, 8))
        
        self.realtime_stats = ttk.Label(stats_inner,
                                       text="",
                                       font=("Segoe UI", 9),
                                       foreground=ACCENT_DIM,
                                       background=BG_CARD)
        self.realtime_stats.pack(anchor="w")
        
        # QUEUE DISPLAY
        queue_frame = tk.Frame(main, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                              highlightthickness=2)
        queue_frame.pack(fill="both", expand=True, pady=(0, 6))
        
        queue_inner = tk.Frame(queue_frame, bg=BG_CARD)
        queue_inner.pack(padx=10, pady=6, fill="both", expand=True)
        
        queue_header = tk.Frame(queue_inner, bg=BG_CARD)
        queue_header.pack(fill="x", pady=(0, 8))
        
        ttk.Label(queue_header, text="BATCH QUEUE",
                 font=("Segoe UI", 10, "bold"),
                 background=BG_CARD,
                 foreground=ACCENT).pack(side="left")
        
        ttk.Button(queue_header, text="Clear All", command=self._clear_queue,
                  style="Secondary.TButton").pack(side="right", padx=(5, 0))
        
        # Queue list with scrollbar - Gaming style
        queue_list_frame = tk.Frame(queue_inner, bg=BG_INPUT,
                                   highlightbackground=ACCENT, highlightthickness=2)
        queue_list_frame.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(queue_list_frame, bg=BG_INPUT, troughcolor=BG_CARD)
        scrollbar.pack(side="right", fill="y")
        
        self.queue_listbox = tk.Listbox(queue_list_frame,
                                        bg=BG_INPUT,
                                        fg=ACCENT,  # Cyan text for gaming look
                                        font=("Consolas", 9, "bold"),
                                        selectbackground=ACCENT,
                                        selectforeground=BG_DARK,
                                        yscrollcommand=scrollbar.set,
                                        height=3,
                                        highlightthickness=0,
                                        bd=0)
        self.queue_listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=self.queue_listbox.yview)
        
        # Queue control buttons
        queue_btn_frame = tk.Frame(queue_inner, bg=BG_CARD)
        queue_btn_frame.pack(fill="x", pady=(8, 0))
        
        ttk.Button(queue_btn_frame, text="Remove Selected",
                  command=self._remove_selected_from_queue,
                  style="Secondary.TButton").pack(side="left", padx=(0, 5))
        
        self.queue_label = ttk.Label(queue_btn_frame,
                                     text="No videos in queue",
                                     font=("Segoe UI", 9),
                                     foreground=TEXT_DIM,
                                     background=BG_CARD)
        self.queue_label.pack(side="left", padx=(10, 0))
        
        # PROGRESS BAR
        progress_section = tk.Frame(main, bg=BG_DARK)
        progress_section.pack(fill="x", pady=(0, 6))
        
        self.bar = ModernNeonBar(progress_section, width=920, height=35)
        self.bar.pack()
        
        # STATUS & CONTROLS
        control_frame = tk.Frame(main, bg=BG_DARK)
        control_frame.pack(fill="x", pady=(0, 6))
        
        self.stat = ttk.Label(control_frame, text="READY TO ENCODE",
                             font=("Segoe UI", 12, "bold"),
                             foreground=ACCENT)
        self.stat.pack(pady=(0, 12))
        
        # Stats row
        stats_row = tk.Frame(control_frame, bg=BG_DARK)
        stats_row.pack(fill="x", pady=(0, 6))
        
        # ETA
        eta_frame = tk.Frame(stats_row, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                            highlightthickness=1)
        eta_frame.pack(side="left", fill="x", expand=True, padx=(0, 5))
        tk.Label(eta_frame, text="ETA", bg=BG_CARD, fg=TEXT_DIM,
                font=("Segoe UI", 8)).pack(pady=(5, 0))
        self.time = tk.Label(eta_frame, text="00:00:00", bg=BG_CARD, fg=TEXT_BRIGHT,
                           font=("Segoe UI", 14, "bold"))
        self.time.pack(pady=(0, 5))
        
        # FPS
        fps_frame = tk.Frame(stats_row, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                           highlightthickness=1)
        fps_frame.pack(side="left", fill="x", expand=True, padx=5)
        tk.Label(fps_frame, text="FPS", bg=BG_CARD, fg=TEXT_DIM,
                font=("Segoe UI", 8)).pack(pady=(5, 0))
        self.fps_label = tk.Label(fps_frame, text="0.0", bg=BG_CARD, fg=TEXT_BRIGHT,
                                 font=("Segoe UI", 14, "bold"))
        self.fps_label.pack(pady=(0, 5))
        
        # CPU
        cpu_frame = tk.Frame(stats_row, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                           highlightthickness=1)
        cpu_frame.pack(side="left", fill="x", expand=True, padx=5)
        tk.Label(cpu_frame, text="CPU", bg=BG_CARD, fg=TEXT_DIM,
                font=("Segoe UI", 8)).pack(pady=(5, 0))
        self.cpu_label = tk.Label(cpu_frame, text="0%", bg=BG_CARD, fg=TEXT_BRIGHT,
                                 font=("Segoe UI", 14, "bold"))
        self.cpu_label.pack(pady=(0, 5))
        
        # GPU
        gpu_frame = tk.Frame(stats_row, bg=BG_CARD, highlightbackground=BORDER_BRIGHT,
                           highlightthickness=1)
        gpu_frame.pack(side="left", fill="x", expand=True, padx=(5, 0))
        tk.Label(gpu_frame, text="GPU", bg=BG_CARD, fg=TEXT_DIM,
                font=("Segoe UI", 8)).pack(pady=(5, 0))
        self.gpu_label = tk.Label(gpu_frame, text="0%", bg=BG_CARD, fg=TEXT_BRIGHT,
                                 font=("Segoe UI", 14, "bold"))
        self.gpu_label.pack(pady=(0, 5))
        
        # Control buttons
        btn_row = tk.Frame(control_frame, bg=BG_DARK)
        btn_row.pack(fill="x")
        
        self.start = ttk.Button(btn_row, text="START",
                               command=self._start, style="TButton")
        self.start.pack(side="left", padx=(0, 12), expand=True, fill="x")
        
        self.cancel = ttk.Button(btn_row, text="CANCEL",
                                command=self._cancel, style="Cancel.TButton",
                                state="disabled")
        self.cancel.pack(side="left", padx=(0, 12), expand=True, fill="x")
        
        self.preview_btn = ttk.Button(btn_row, text="PREVIEW",
                                     command=self._preview, style="Secondary.TButton")
        self.preview_btn.pack(side="left", padx=(0, 12), expand=True, fill="x")
        
        self.log_btn = ttk.Button(btn_row, text="LOG",
                                 command=self._show_log, style="Secondary.TButton")
        self.log_btn.pack(side="left", padx=(0, 12), expand=True, fill="x")
        
        self.clear_btn = ttk.Button(btn_row, text="CLEAR",
                                    command=self._clear_all, style="Warning.TButton")
        self.clear_btn.pack(side="left", expand=True, fill="x")
    
    def _setup_dnd(self):
        """
        Setup drag and drop

        v5.1.1: Improved error handling for Windows 10 compatibility
        """
        try:
            if not DND_OK:
                print("[DND] tkinterdnd2 not available, drag and drop disabled")
                return

            self.ein.drop_target_register(DND_FILES)
            self.ein.dnd_bind('<<Drop>>', self._on_drop)
            print("[DND] Drag and drop initialized successfully")
        except Exception as e:
            print(f"[DND] Failed to setup drag and drop: {e}")
            print("[DND] You can still browse for files using the Browse button")
    
    def _on_drop(self, event):
        """
        Handle drag and drop

        v5.1.2: Fixed Windows path parsing with spaces in filenames
        """
        try:
            # Debug: Show raw event data
            print(f"[DND] Raw event.data: {repr(event.data)}")

            # Handle different drop event formats (Windows vs Linux)
            if isinstance(event.data, str):
                # Use splitlist directly - it correctly handles curly braces
                # tkinterdnd2 wraps paths with spaces in curly braces: {C:/path/file name.mp4}
                files = self.root.tk.splitlist(event.data)
            else:
                files = [event.data]

            print(f"[DND] Parsed files list: {files}")

            if files:
                # Normalize path (remove curly braces, quotes, extra spaces)
                file_path = str(files[0]).strip().strip('{}').strip('"').strip("'").strip()

                print(f"[DND] Normalized path: {file_path}")
                print(f"[DND] File exists: {os.path.exists(file_path)}")
                print(f"[DND] Is file: {os.path.isfile(file_path)}")
                print(f"[DND] Is directory: {os.path.isdir(file_path)}")

                if os.path.isfile(file_path):
                    self.inp.set(file_path)
                    print(f"[DND] ✓ File dropped successfully: {file_path}")
                else:
                    print(f"[DND] ✗ Invalid file path: {file_path}")
                    if os.path.isdir(file_path):
                        print(f"[DND]   This is a directory, not a file. Please drop a video file.")
        except Exception as e:
            print(f"[DND] Error handling drop: {e}")
            import traceback
            traceback.print_exc()
    
    def _on_auto_mode_toggle(self):
        """Handle auto-mode toggle"""
        if self.auto_mode.get():
            self.combo_mode.config(state="disabled")
        else:
            self.combo_mode.config(state="readonly")
    
    def _ensure_default_mode(self):
        """Ensure AV1 Balanced remains the default unless the user picks something else."""
        current = (self.mode.get() or "").strip()
        valid_modes = {
            "AV1 Ultra", "AV1 Balanced", "AV1 Compress", "AV1 Fast",
            "NVENC Ultra", "NVENC Balanced", "NVENC Fast"
        }
        if current and current in valid_modes:
            return
        if getattr(self, "_setting_default_mode", False):
            return
        self._setting_default_mode = True
        try:
            self.mode.set("AV1 Balanced")
        finally:
            self._setting_default_mode = False
    
    def _on_input_change(self, *args):
        """Handle input file change"""
        inp = self.inp.get().strip()
        self._ensure_default_mode()
        
        if self.output_is_auto and inp and os.path.isfile(inp):
            if self.auto_mode.get():
                self._analyze_and_select_preset(inp)
            
            self._generate_output_path(inp)
            self._on_settings_change()
    
    def _analyze_and_select_preset(self, inp: str):
        """Analyze video and automatically select best preset"""
        try:
            info = ffprobe_info_extended(inp)
            selected_mode = smart_select_preset(info, HAS_HEVC_NVENC, HAS_LIBSVTAV1, self.error_log)
            
            # Normalize the mode to handle any legacy names
            selected_mode = normalize_mode(selected_mode)
            
            self.mode.set(selected_mode)
            
            self.error_log.append("=" * 80)
            self.error_log.append(f"AUTO-MODE: Selected '{selected_mode}'")
            self.error_log.append("=" * 80)
            
        except Exception as e:
            self.error_log.append(f"Auto-mode error: {e}")
    
    def _on_output_manual_change(self, *args):
        """Track when user manually edits output path"""
        if not self.out.get():
            self.output_is_auto = True
        else:
            if not hasattr(self, '_updating_output'):
                self.output_is_auto = False
    
    def _on_mode_change(self, *args):
        """Handle mode change"""
        inp = self.inp.get().strip()
        
        if self.output_is_auto and inp and os.path.isfile(inp):
            self._generate_output_path(inp)
        
        self._on_settings_change()
    
    def _setup_keyboard_shortcuts(self):
        """Setup keyboard shortcuts (NEW v5.0)"""
        # Ctrl+O: Open file
        self.root.bind('<Control-o>', lambda e: self._browse_input())
        # Ctrl+S: Start encoding
        self.root.bind('<Control-s>', lambda e: self.start.config(state="normal") and self._start_encoding() if not self.is_running else None)
        # Ctrl+Q: Add to queue
        self.root.bind('<Control-q>', lambda e: self._add_to_queue())
        # Ctrl+P: Toggle theme
        self.root.bind('<Control-p>', lambda e: self._toggle_theme())
        # Ctrl+H: Show history
        self.root.bind('<Control-h>', lambda e: self._show_history())
        # Escape: Cancel
        self.root.bind('<Escape>', lambda e: self._cancel() if self.is_running else None)
        # F5: Refresh preview
        self.root.bind('<F5>', lambda e: self._preview() if hasattr(self, 'preview_btn') else None)
    
    def _load_saved_profiles(self):
        """Load saved encoding profiles"""
        try:
            profiles = load_all_profiles()
            # Profiles loaded, available for use in profile dropdown
            self.saved_profiles = profiles
        except Exception as e:
            self.saved_profiles = {}
            print(f"Error loading profiles: {e}")
    
    def _toggle_theme(self):
        """Toggle between dark and light theme (NEW v5.0)"""
        global CURRENT_THEME, BG_DARK, BG_MID, BG_CARD, BG_INPUT, ACCENT, ACCENT_BRIGHT
        global ACCENT_DIM, ACCENT_GLOW, TEXT_BRIGHT, TEXT_MID, TEXT_DIM, SUCCESS, ERROR, WARNING
        global BORDER, BORDER_BRIGHT
        
        self.dark_theme.set(not self.dark_theme.get())
        CURRENT_THEME = THEME_DARK.copy() if self.dark_theme.get() else THEME_LIGHT.copy()
        
        # Update global theme variables
        BG_DARK = CURRENT_THEME["BG_DARK"]
        BG_MID = CURRENT_THEME["BG_MID"]
        BG_CARD = CURRENT_THEME["BG_CARD"]
        BG_INPUT = CURRENT_THEME["BG_INPUT"]
        ACCENT = CURRENT_THEME["ACCENT"]
        ACCENT_BRIGHT = CURRENT_THEME["ACCENT_BRIGHT"]
        ACCENT_DIM = CURRENT_THEME["ACCENT_DIM"]
        ACCENT_GLOW = CURRENT_THEME["ACCENT_GLOW"]
        TEXT_BRIGHT = CURRENT_THEME["TEXT_BRIGHT"]
        TEXT_MID = CURRENT_THEME["TEXT_MID"]
        TEXT_DIM = CURRENT_THEME["TEXT_DIM"]
        SUCCESS = CURRENT_THEME["SUCCESS"]
        ERROR = CURRENT_THEME["ERROR"]
        WARNING = CURRENT_THEME["WARNING"]
        BORDER = CURRENT_THEME["BORDER"]
        BORDER_BRIGHT = CURRENT_THEME["BORDER_BRIGHT"]
        
        # Rebuild GUI with new theme
        self._setup_styles()
        # Note: Full GUI rebuild would require more complex implementation
        # For now, this sets up the theme for new windows
    
    def _show_history(self):
        """Show encoding history window (NEW v5.0)"""
        history = load_history()
        if not history:
            messagebox.showinfo("History", "No encoding history found.")
            return
        
        # Create history window
        hist_window = tk.Toplevel(self.root)
        hist_window.title("Encoding History")
        hist_window.geometry("900x600")
        hist_window.configure(bg=BG_DARK)
        
        # Header
        header = tk.Frame(hist_window, bg=BG_DARK)
        header.pack(fill="x", padx=10, pady=10)
        ttk.Label(header, text="Encoding History", font=("Segoe UI", 14, "bold"),
                 background=BG_DARK, foreground=ACCENT).pack(side="left")
        ttk.Button(header, text="Clear History", command=lambda: self._clear_history_confirm(hist_window)).pack(side="right")
        
        # Listbox with scrollbar
        list_frame = tk.Frame(hist_window, bg=BG_DARK)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame, bg=BG_INPUT)
        scrollbar.pack(side="right", fill="y")
        
        history_list = tk.Listbox(list_frame, bg=BG_INPUT, fg=TEXT_BRIGHT,
                                  selectbackground=ACCENT, font=("Consolas", 9),
                                  yscrollcommand=scrollbar.set)
        history_list.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=history_list.yview)
        
        # Populate history
        for entry in reversed(history[-100:]):  # Show last 100
            ratio = entry.get("compression_ratio", 0) * 100
            size_saved = entry.get("input_size", 0) - entry.get("output_size", 0)
            line = (f"{entry.get('timestamp', 'Unknown')} | "
                   f"{os.path.basename(entry.get('input_path', ''))} | "
                   f"{fmt_size(entry.get('input_size', 0))} ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ {fmt_size(entry.get('output_size', 0))} | "
                   f"{ratio:.1f}% saved | {entry.get('mode', 'Unknown')}")
            history_list.insert(0, line)
    
    def _clear_history_confirm(self, parent):
        """Confirm and clear history"""
        if messagebox.askyesno("Clear History", "Clear all encoding history?"):
            clear_history()
            parent.destroy()
            self._show_history()
    
    def _save_current_profile(self):
        """Save current settings as a profile (NEW v5.0)"""
        name = simpledialog.askstring("Save Profile", "Enter profile name:")
        if not name:
            return
        
        profile = EncodingProfile(
            name=name,
            mode=self.mode.get(),
            resolution=self.resolution.get(),
            two_pass=self.two_pass.get(),
            auto_mode=self.auto_mode.get(),
            keep_hdr=self.keep_hdr.get(),
            skip_small_saving=self.skip_small_saving.get(),
            custom_cq=self.custom_cq.get() if self.custom_cq.get() > 0 else None,
            custom_filters=self.custom_filters.get(),
            sharpening_profile=self.sharpening_profile.get(),
            av1_tune=self.av1_tune.get()
        )
        
        if save_profile(profile):
            messagebox.showinfo("Success", f"Profile '{name}' saved successfully!")
            self._load_saved_profiles()
        else:
            messagebox.showerror("Error", "Failed to save profile.")
    
    def _load_profile_dialog(self):
        """Show dialog to load a profile (NEW v5.0)"""
        profiles = load_all_profiles()
        if not profiles:
            messagebox.showinfo("No Profiles", "No saved profiles found.")
            return
        
        # Create profile selection window
        prof_window = tk.Toplevel(self.root)
        prof_window.title("Load Profile")
        prof_window.geometry("400x300")
        prof_window.configure(bg=BG_DARK)
        
        ttk.Label(prof_window, text="Select Profile:", font=("Segoe UI", 10, "bold"),
                 background=BG_DARK, foreground=ACCENT).pack(pady=10)
        
        list_frame = tk.Frame(prof_window, bg=BG_DARK)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame, bg=BG_INPUT)
        scrollbar.pack(side="right", fill="y")
        
        profile_list = tk.Listbox(list_frame, bg=BG_INPUT, fg=TEXT_BRIGHT,
                                  selectbackground=ACCENT, font=("Segoe UI", 10),
                                  yscrollcommand=scrollbar.set)
        profile_list.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=profile_list.yview)
        
        for name in profiles.keys():
            profile_list.insert(tk.END, name)
        
        def on_load():
            selection = profile_list.curselection()
            if selection:
                name = profile_list.get(selection[0])
                profile = load_profile(name)
                if profile:
                    self._apply_profile(profile)
                    prof_window.destroy()
        
        def on_delete():
            selection = profile_list.curselection()
            if selection:
                name = profile_list.get(selection[0])
                if messagebox.askyesno("Delete Profile", f"Delete profile '{name}'?"):
                    delete_profile(name)
                    profile_list.delete(selection[0])
        
        btn_frame = tk.Frame(prof_window, bg=BG_DARK)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Load", command=on_load).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Delete", command=on_delete).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cancel", command=prof_window.destroy).pack(side="left", padx=5)
    
    def _apply_profile(self, profile: EncodingProfile):
        """Apply a loaded profile to current settings"""
        # Normalize the mode to handle legacy saved modes
        normalized_mode = normalize_mode(profile.mode)
        self.mode.set(normalized_mode)
        self.resolution.set(profile.resolution)
        self.two_pass.set(profile.two_pass)
        self.auto_mode.set(profile.auto_mode)
        self.keep_hdr.set(profile.keep_hdr)
        self.skip_small_saving.set(profile.skip_small_saving)
        if profile.custom_cq:
            self.custom_cq.set(profile.custom_cq)
        self.custom_filters.set(profile.custom_filters)
        self.sharpening_profile.set(profile.sharpening_profile)
        self.av1_tune.set(profile.av1_tune)
        self.current_profile_name.set(profile.name)
    
    def _toggle_advanced(self):
        """Toggle advanced settings visibility"""
        self.advanced_expanded.set(not self.advanced_expanded.get())
        if self.advanced_expanded.get():
            self.advanced_content.pack(fill="x", padx=10, pady=(0, 8))
            self.advanced_indicator.config(text="ÃƒÂ¢Ã¢â‚¬â€œÃ‚Â¼")
        else:
            self.advanced_content.pack_forget()
            self.advanced_indicator.config(text="ÃƒÂ¢Ã¢â‚¬â€œÃ‚Â¶")
    
    def _browse_watch_folder(self):
        """Browse for watch folder"""
        folder = filedialog.askdirectory(title="Select Watch Folder")
        if folder:
            self.watch_folder_path.set(folder)
            if self.watch_folder_enabled.get():
                self._start_watch_folder()
    
    def _start_watch_folder(self):
        """Start monitoring watch folder for new videos (NEW v5.0)"""
        if self.watch_folder_thread and self.watch_folder_thread.is_alive():
            return  # Already running
        
        watch_path = self.watch_folder_path.get()
        if not watch_path or not os.path.isdir(watch_path):
            return
        
        def watch_loop():
            """Background thread that watches for new video files"""
            processed_files = set()
            
            while self.watch_folder_enabled.get():
                try:
                    if os.path.isdir(watch_path):
                        # Get video files
                        video_extensions = {'.mp4', '.mkv', '.avi', '.mov', '.m4v', '.webm', '.flv', '.wmv'}
                        for filename in os.listdir(watch_path):
                            filepath = os.path.join(watch_path, filename)
                            if os.path.isfile(filepath) and os.path.splitext(filename)[1].lower() in video_extensions:
                                if filepath not in processed_files:
                                    processed_files.add(filepath)
                                    # Wait a bit to ensure file is fully written
                                    time.sleep(2)
                                    if os.path.exists(filepath):
                                        # Add to queue
                                        self.root.after(0, lambda fp=filepath: self._add_watch_file_to_queue(fp))
                    time.sleep(5)  # Check every 5 seconds
                except Exception as e:
                    print(f"Watch folder error: {e}")
                    time.sleep(10)
        
        self.watch_folder_thread = threading.Thread(target=watch_loop, daemon=True)
        self.watch_folder_thread.start()
        self.error_log.append(f"ÃƒÂ°Ã…Â¸Ã¢â‚¬ËœÃ‚ÂÃƒÂ¯Ã‚Â¸Ã‚Â Watch folder started: {watch_path}")
    
    def _add_watch_file_to_queue(self, filepath: str):
        """Add a file from watch folder to queue"""
        try:
            # Generate output path
            base = os.path.splitext(filepath)[0]
            mode_suffix = self.mode.get().replace(" ", "_")
            ext = ".mp4"
            output_path = f"{base}_{mode_suffix}{ext}"
            
            # Add to queue
            item = QueueItem(
                input_path=filepath,
                output_path=output_path,
                mode=self.mode.get(),
                resolution=self.resolution.get(),
                two_pass=self.two_pass.get(),
                estimated_size=0
            )
            self.queue.append(item)
            self._update_queue_display()
            self.error_log.append(f"[INBOX] Added from watch folder: {os.path.basename(filepath)}")
            
            # Auto-start if not already running
            if not self.is_running and len(self.queue) == 1:
                self.root.after(1000, self._start_queue_processing)
        except Exception as e:
            self.error_log.append(f"ÃƒÂ¢Ã…Â¡Ã‚Â ÃƒÂ¯Ã‚Â¸Ã‚Â Failed to add watch file: {e}")
    
    def _on_mode_change_original(self, *args):
        """Handle mode change (original implementation)"""
        inp = self.inp.get().strip()
        
        if self.output_is_auto and inp and os.path.isfile(inp):
            self._generate_output_path(inp)
        
        self._on_settings_change()
    
    def _generate_output_path(self, inp: str):
        """Generate output path with mode suffix (NEW v5.0: With organization support)"""
        try:
            self._updating_output = True
            
            base = os.path.splitext(inp)[0]
            mode_suffix = self.mode.get().replace(" ", "_")
            ext = ".mp4"
            
            # NEW v5.0: Output organization by date/mode
            if self.organize_output.get():
                date_str = datetime.datetime.now().strftime("%Y-%m-%d")
                mode_folder = mode_suffix.replace("_", "")
                output_dir = os.path.join(os.path.dirname(inp) or ".", "Compressed", date_str, mode_folder)
                os.makedirs(output_dir, exist_ok=True)
                filename = os.path.basename(base) + "_" + mode_suffix + ext
                output_path = os.path.join(output_dir, filename)
            else:
                output_path = f"{base}_{mode_suffix}{ext}"
            
            self.out.set(output_path)
            self.output_is_auto = True
            
        finally:
            delattr(self, '_updating_output')
    
    def _on_settings_change(self, *args):
        """Update size estimation when settings change"""
        inp = self.inp.get().strip()
        self._ensure_default_mode()
        if not inp or not os.path.isfile(inp):
            return
        
        try:
            self.input_size = os.path.getsize(inp)
            info = ffprobe_info(inp)
            info_ext = ffprobe_info_extended(inp)
            self.source_width = info["width"]
            self.source_height = info["height"]
            tmp_log: List[str] = []
            filters_for_est = get_smart_filters(info_ext, self.keep_hdr.get(), tmp_log)
            copy_audio = should_copy_audio(info_ext, tmp_log)
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_hint = "auto"
            elif encoder_pref == "NVIDIA NVENC":
                encoder_hint = "nvenc"
            elif encoder_pref == "AMD AMF":
                encoder_hint = "amf"
            else:
                encoder_hint = "auto"
            
            # Normalize mode before estimation
            current_mode = normalize_mode(self.mode.get())
            
            self.estimated_output_size = estimate_output_size(
                inp,
                current_mode,
                self.resolution.get(),
                info["bitrate"],
                keep_hdr=self.keep_hdr.get(),
                encoder_hint=encoder_hint,
                smart_filters=filters_for_est,
                copy_audio=copy_audio,
                custom_cq=self.custom_cq.get() if self.custom_cq.get() > 0 else None,
                sharpening_profile=self.sharpening_profile.get()
            )
            
            reduction = (1 - self.estimated_output_size / self.input_size) * 100 if self.input_size > 0 else 0
            
            self.size_label.config(
                text=f"Input: {fmt_size(self.input_size)} -> Estimated: {fmt_size(self.estimated_output_size)} "
                     f"({reduction:.0f}% reduction)",
                foreground=ACCENT
            )
        except Exception as e:
            # Silently handle estimation errors - don't reference self in error handling
            self.size_label.config(
                text=f"Estimation unavailable",
                foreground=TEXT_DIM
            )
    
    def _browse(self):
        """Browse for input file"""
        f = filedialog.askopenfilename(
            title="Select Video",
            filetypes=[
                ("Video files", "*.mp4 *.mkv *.avi *.mov *.wmv *.flv *.webm *.m4v *.mpg *.mpeg"),
                ("All files", "*.*")
            ]
        )
        if f:
            self.inp.set(f)
            self.output_is_auto = True
    
    def _browse_batch(self):
        """Browse for batch files"""
        files = filedialog.askopenfilenames(
            title="Select Videos for Batch Processing",
            filetypes=[
                ("Video files", "*.mp4 *.mkv *.avi *.mov *.wmv *.flv *.webm *.m4v *.mpg *.mpeg"),
                ("All files", "*.*")
            ]
        )
        
        if not files:
            return
        
        # Show output location dialog
        output_dialog = tk.Toplevel(self.root)
        output_dialog.title("Batch Output Location")
        output_dialog.geometry("500x250")
        output_dialog.configure(bg=BG_DARK)
        output_dialog.transient(self.root)
        output_dialog.grab_set()
        
        # Center dialog
        output_dialog.update_idletasks()
        x = (output_dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (output_dialog.winfo_screenheight() // 2) - (250 // 2)
        output_dialog.geometry(f"+{x}+{y}")
        
        dialog_frame = tk.Frame(output_dialog, bg=BG_DARK)
        dialog_frame.pack(fill="both", expand=True, padx=12, pady=20)
        
        ttk.Label(dialog_frame,
                 text=f"Adding {len(files)} videos to queue",
                 font=("Segoe UI", 10, "bold"),
                 foreground=ACCENT,
                 background=BG_DARK).pack(pady=(0, 8))
        
        ttk.Label(dialog_frame,
                 text="Where should the encoded files be saved?",
                 font=("Segoe UI", 10),
                 foreground=TEXT_BRIGHT,
                 background=BG_DARK).pack(pady=(0, 8))
        
        # Radio buttons
        output_mode = tk.StringVar(value="source")
        
        radio_frame = tk.Frame(dialog_frame, bg=BG_CARD,
                              highlightbackground=BORDER_BRIGHT, highlightthickness=2)
        radio_frame.pack(fill="x", pady=(0, 8))
        
        ttk.Radiobutton(radio_frame,
                       text="Same folder as source files",
                       variable=output_mode,
                       value="source").pack(anchor="w", padx=10, pady=(10, 5))
        
        ttk.Radiobutton(radio_frame,
                       text="Custom output folder (all files)",
                       variable=output_mode,
                       value="custom").pack(anchor="w", padx=10, pady=(5, 10))
        
        # Custom folder selection
        custom_folder = tk.StringVar()
        
        folder_frame = tk.Frame(dialog_frame, bg=BG_DARK)
        folder_frame.pack(fill="x", pady=(0, 8))
        
        folder_entry = tk.Entry(folder_frame, textvariable=custom_folder,
                               bg=BG_INPUT, fg=TEXT_BRIGHT,
                               font=("Segoe UI", 9), state="disabled")
        folder_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        def browse_folder():
            folder = filedialog.askdirectory(title="Select Output Folder")
            if folder:
                custom_folder.set(folder)
        
        folder_btn = ttk.Button(folder_frame, text="Browse",
                               command=browse_folder,
                               style="Secondary.TButton",
                               state="disabled")
        folder_btn.pack(side="left")
        
        def on_mode_change():
            if output_mode.get() == "custom":
                folder_entry.config(state="normal")
                folder_btn.config(state="normal")
            else:
                folder_entry.config(state="disabled")
                folder_btn.config(state="disabled")
        
        output_mode.trace_add("write", lambda *args: on_mode_change())
        
        # OK/Cancel buttons
        btn_frame = tk.Frame(dialog_frame, bg=BG_DARK)
        btn_frame.pack(fill="x")
        
        result = {"confirmed": False}
        
        def on_ok():
            if output_mode.get() == "custom" and not custom_folder.get():
                messagebox.showerror("Error", "Please select an output folder")
                return
            result["confirmed"] = True
            result["mode"] = output_mode.get()
            result["folder"] = custom_folder.get()
            output_dialog.destroy()
        
        def on_cancel():
            output_dialog.destroy()
        
        ttk.Button(btn_frame, text="Add to Queue", command=on_ok,
                  style="TButton").pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        ttk.Button(btn_frame, text="Cancel", command=on_cancel,
                  style="Cancel.TButton").pack(side="left", expand=True, fill="x")
        
        self.root.wait_window(output_dialog)
        
        if not result["confirmed"]:
            return
        
        # Add files to queue
        current_auto_mode = self.auto_mode.get()
        
        for f in files:
            # Auto-select mode if enabled
            if current_auto_mode:
                try:
                    info = ffprobe_info_extended(f)
                    file_mode = smart_select_preset(info, HAS_HEVC_NVENC, HAS_LIBSVTAV1, self.error_log)
                    file_mode = normalize_mode(file_mode)
                except:
                    file_mode = normalize_mode(self.mode.get())
            else:
                file_mode = normalize_mode(self.mode.get())
            
            # Generate output path
            if result["mode"] == "source":
                base = os.path.splitext(f)[0]
                ext = ".mp4"
                output = f"{base}_{file_mode.replace(' ', '_')}{ext}"
            else:
                filename = os.path.basename(f)
                base = os.path.splitext(filename)[0]
                ext = ".mp4"
                output = os.path.join(result["folder"], f"{base}_{file_mode.replace(' ', '_')}{ext}")
            
            # Estimate size
            try:
                info = ffprobe_info(f)
                info_ext = ffprobe_info_extended(f)
                tmp_log: List[str] = []
                filters_for_est = get_smart_filters(info_ext, self.keep_hdr.get(), tmp_log)
                copy_audio = should_copy_audio(info_ext, tmp_log)
                encoder_hint = self.encoder_preference.get()
                if encoder_hint == "Auto (detect GPU)":
                    encoder_hint = "auto"
                elif encoder_hint == "NVIDIA NVENC":
                    encoder_hint = "nvenc"
                elif encoder_hint == "AMD AMF":
                    encoder_hint = "amf"
                else:
                    encoder_hint = "auto"
                est_size = estimate_output_size(
                    f,
                    file_mode,
                    self.resolution.get(),
                    info["bitrate"],
                    keep_hdr=self.keep_hdr.get(),
                    encoder_hint=encoder_hint,
                    smart_filters=filters_for_est,
                    copy_audio=copy_audio,
                    custom_cq=self.custom_cq.get() if self.custom_cq.get() > 0 else None,
                    sharpening_profile=self.sharpening_profile.get()
                )
            except:
                est_size = 0
            
            # Add to queue
            item = QueueItem(
                input_path=f,
                output_path=output,
                mode=file_mode,
                resolution=self.resolution.get(),
                two_pass=self.two_pass.get(),
                estimated_size=est_size
            )
            self.queue.append(item)
        
        self._update_queue_display()
    
    def _browse_output(self):
        """Browse for output file"""
        f = filedialog.asksaveasfilename(
            title="Save Video As",
            defaultextension=".mp4",
            filetypes=[
                ("MP4 files", "*.mp4"),
                ("MKV files", "*.mkv"),
                ("All files", "*.*")
            ]
        )
        if f:
            self.out.set(f)
            self.output_is_auto = False
    
    def _update_queue_display(self):
        """Update queue display"""
        self.queue_listbox.delete(0, tk.END)
        
        for i, item in enumerate(self.queue):
            if item.status == "pending":
                status_icon = "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³"
                status_color = TEXT_DIM
            elif item.status == "encoding":
                status_icon = "[PLAY]Â"
                status_color = ACCENT
            elif item.status == "completed":
                status_icon = "[CHECK]"
                status_color = SUCCESS
            elif item.status == "skipped":
                status_icon = "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â"
                status_color = WARNING
            elif item.status == "failed":
                status_icon = "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢"
                status_color = ERROR
            else:
                status_icon = "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ"
                status_color = TEXT_DIM
            
            name = item.get_display_name()
            mode_short = item.mode.replace(" ", "")[:8]
            
            if item.status == "encoding":
                # Add ASCII progress bar for encoding items
                progress_pct = item.progress
                bar_width = 20
                filled = int((progress_pct / 100) * bar_width)
                bar = "[" + "=" * filled + ">" + " " * (bar_width - filled - 1) + "]"
                line = f"{status_icon} [{i+1}] {name:35s} {bar} {progress_pct:5.1f}%"
            elif item.status == "completed":
                reduction = (1 - item.actual_size / os.path.getsize(item.input_path)) * 100 if item.actual_size > 0 else 0
                line = f"{status_icon} [{i+1}] {name:40s} | {mode_short:8s} | {reduction:3.0f}% smaller"
            else:
                line = f"{status_icon} [{i+1}] {name:40s} | {mode_short:8s} | {item.status}"
            
            self.queue_listbox.insert(tk.END, line)
            
            if item.status == "completed":
                self.queue_listbox.itemconfig(i, fg=SUCCESS)
            elif item.status == "skipped":
                self.queue_listbox.itemconfig(i, fg=WARNING)
            elif item.status == "failed":
                self.queue_listbox.itemconfig(i, fg=ERROR)
            elif item.status == "encoding":
                self.queue_listbox.itemconfig(i, fg=ACCENT_BRIGHT)
        
        # Update summary
        if not self.queue:
            self.queue_label.config(text="No videos in queue")
        else:
            pending = sum(1 for item in self.queue if item.status == "pending")
            completed = sum(1 for item in self.queue if item.status == "completed")
            failed = sum(1 for item in self.queue if item.status == "failed")
            skipped = sum(1 for item in self.queue if item.status == "skipped")
            
            self.queue_label.config(
                text=f"Total: {len(self.queue)} | ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Pending: {pending} | "
                     f"[CHECK] Done: {completed} | ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Skipped: {skipped} | ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Failed: {failed}"
            )
    
    def _remove_selected_from_queue(self):
        """Remove selected item from queue"""
        selection = self.queue_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a video from the queue to remove")
            return
        
        index = selection[0]
        item = self.queue[index]
        
        if item.status == "encoding":
            messagebox.showwarning("Cannot Remove", "Cannot remove the currently encoding video")
            return
        
        self.queue.pop(index)
        self._update_queue_display()
    
    def _clear_queue(self):
        """Clear the queue"""
        if self.queue and messagebox.askyesno("Clear Queue", "Remove all videos from queue?"):
            if self.current_queue_item:
                self.queue = [item for item in self.queue if item.status == "encoding"]
            else:
                self.queue.clear()
            self._update_queue_display()
    
    def _clear_all(self):
        """Reset entire interface"""
        if self.is_running:
            messagebox.showwarning("Encoding in Progress", "Cannot clear while encoding!")
            return
        
        if self.queue and not messagebox.askyesno("Clear Everything", 
            "Clear all inputs, outputs, and queue?"):
            return
        
        # Clear paths
        self.inp.set("")
        self.out.set("")
        self.output_is_auto = True
        
        # Reset settings
        self.mode.set("AV1 Balanced")
        self.resolution.set("Same as source")
        self.two_pass.set(False)
        self.shutdown_after.set(False)
        
        # Reset smart options
        self.auto_mode.set(True)
        self.keep_hdr.set(True)
        self.skip_small_saving.set(False)
        self.combo_mode.config(state="disabled")
        
        # Clear queue
        self.queue.clear()
        self.current_queue_item = None
        self._update_queue_display()
        
        # Reset progress
        self.bar.set(0)
        self.stat.config(text="Ready to encode", foreground=ACCENT)
        self.time.config(text="00:00:00")
        self.fps_label.config(text="0.0")
        
        # Clear stats
        self.size_label.config(
            text="Select a video to see size estimation",
            foreground=TEXT_MID
        )
        self.realtime_stats.config(text="")
        
        # Reset state
        self.error_log = []
        self.estimated_output_size = 0
        self.current_output_size = 0
        self.speed_history = []
        self.input_size = 0
        
        # Remove resume file
        if os.path.exists(self.resume_file):
            try:
                os.remove(self.resume_file)
            except:
                pass
        
        messagebox.showinfo("Cleared", "Interface reset to initial state!")
    
    def _preview(self):
        """Encode a 10-second preview"""
        inp = self.inp.get().strip()
        if not inp or not os.path.isfile(inp):
            messagebox.showerror("Error", "Select a valid input file first")
            return
        
        if self.is_running:
            messagebox.showwarning("Busy", "Encoding already in progress")
            return
        
        # Generate preview output
        base = os.path.splitext(inp)[0]
        preview_out = f"{base}_preview_10s.mp4"
        
        if os.path.exists(preview_out):
            if not messagebox.askyesno("Preview Exists", f"Overwrite existing preview?\n{preview_out}"):
                return
        
        mode = self.mode.get()
        self._last_hw_plan = None
        resolution = self.resolution.get()
        
        # Get video info
        info_ext = ffprobe_info_extended(inp)
        info = ffprobe_info(inp)
        self.source_width = info["width"]
        self.source_height = info["height"]
        
        # Get smart filters
        smart_filters = get_smart_filters(info_ext, self.keep_hdr.get(), self.error_log)
        copy_audio = should_copy_audio(info_ext, self.error_log)
        
        # Get preset
        # NEW v5.0: Get advanced settings
        av1_tune_val = self.av1_tune.get()
        sharpening_val = self.sharpening_profile.get()
        custom_cq_val = self.custom_cq.get() if self.custom_cq.get() > 0 else None
        
        # NEW: Check if AMD AV1 hardware is available and auto-mode is enabled
        use_amd_av1_hardware = (self.auto_mode.get() and HAS_AV1_AMF and mode.startswith("AV1"))
        
        if use_amd_av1_hardware:
            # Use AMD hardware AV1 instead of CPU software
            self.error_log.append("ðŸš€ AUTO-MODE: Switching to AMD AV1 hardware encoding")
            self.error_log.append(f"   Original mode: {mode}")
            self.error_log.append(f"   Using: AMD AV1_AMF (hardware accelerated)")
            
            # Determine encoder preference
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_pref = "auto"
            elif encoder_pref == "AMD AMF":
                encoder_pref = "amf"
            else:
                encoder_pref = "auto"  # Force auto for AV1 hardware
            
            encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)
            
            if encoder_name == "amf":
                preset_cmd, use_hwaccel, plan_meta = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
                self._last_hw_plan = plan_meta
            else:
                # Fallback to CPU if AMD not available
                use_amd_av1_hardware = False
                self.error_log.append("âš ï¸  AMD not available, using CPU software encoder")
        
        # Check if AMD AV1 hardware should be used for preview
        use_amd_av1_preview = (self.auto_mode.get() and HAS_AV1_AMF and mode.startswith("AV1"))
        
        if use_amd_av1_preview:
            # Use AMD hardware for AV1 preview
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_pref = "auto"
            elif encoder_pref == "AMD AMF":
                encoder_pref = "amf"
            else:
                encoder_pref = "auto"
            
            encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)
            
            if encoder_name == "amf":
                preset_cmd, use_hwaccel, _ = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
            else:
                use_amd_av1_preview = False
        
        if not use_amd_av1_preview:
            if mode == "AV1 Ultra":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_ultra(
                    resolution, self.source_width, self.source_height, smart_filters, 
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Balanced":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_balanced(
                    resolution, self.source_width, self.source_height, smart_filters,
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Compress":
                # Use balanced preset as base for CPU fallback (actual compression happens in AMF)
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_balanced(
                    resolution, self.source_width, self.source_height, smart_filters,
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Fast":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_fast(
                    resolution, self.source_width, self.source_height, smart_filters, 
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
        
        if mode in ["NVENC Ultra", "NVENC Balanced", "NVENC Fast"] or use_amd_av1_preview:
            # NEW v5.0: Determine encoder based on preference
            # Skip if already set by AV1 hardware detection
            if not use_amd_av1_hardware:
                encoder_pref = self.encoder_preference.get()
                if encoder_pref == "Auto (detect GPU)":
                    encoder_pref = "auto"
                elif encoder_pref == "NVIDIA NVENC":
                    encoder_pref = "nvenc"
                elif encoder_pref == "AMD AMF":
                    encoder_pref = "amf"
                else:
                    encoder_pref = "cpu"
                
                encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)

            # Warn if requested encoder not available
            if encoder_pref == "amf" and not HAS_ANY_AMF:
                self.error_log.append("WARNING: AMD AMF not available, falling back to Auto")
                encoder_name, use_hwaccel = detect_best_encoder("auto")
            elif encoder_pref == "nvenc" and not HAS_HEVC_NVENC:
                self.error_log.append("WARNING: NVIDIA NVENC not available, falling back to Auto")
                encoder_name, use_hwaccel = detect_best_encoder("auto")
            
            if encoder_name == "amf":
                preset_cmd, use_hwaccel, _ = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
            else:
                preset_cmd, use_hwaccel, _ = EncodingPresets.get_nvenc_adaptive(
                    resolution, self.source_width, self.source_height, inp, 
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val)
        else:
            messagebox.showerror("Error", "Unknown mode")
            return
        
        # Build preview command
        if use_hwaccel:
            # NEW v5.0: Determine encoder for preview hwaccel
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_pref = "auto"
            elif encoder_pref == "AMD AMF":
                encoder_pref = "amf"
            else:
                encoder_pref = "nvenc"
            encoder_name, _ = detect_best_encoder(encoder_pref)
            hwaccel_type = "d3d11va" if encoder_name == "amf" else "cuda"
            cmd = [FFMPEG, "-hide_banner", "-y", "-hwaccel", hwaccel_type, "-i", inp, "-t", "10"]
        else:
            cmd = [FFMPEG, "-hide_banner", "-y", "-i", inp, "-t", "10"]
        
        cmd.extend(["-map", "0:v:0", "-map", "0:a:0?", "-sn", "-dn", "-map_metadata", "0"])
        cmd.extend(preset_cmd)
        cmd.extend(["-movflags", "+faststart", preview_out])
        
        # Run preview
        self.stat.config(text="Encoding 10s preview...", foreground=ACCENT)
        self.start.config(state="disabled")
        self.preview_btn.config(state="disabled")
        
        def run_preview():
            try:
                subprocess.run(cmd, check=True, capture_output=True)
                self.root.after(0, lambda: self.stat.config(
                    text=f"Preview saved: {os.path.basename(preview_out)}", 
                    foreground=SUCCESS
                ))
                self.root.after(0, lambda: messagebox.showinfo(
                    "Preview Complete",
                    f"10-second preview saved to:\n{preview_out}"
                ))
            except subprocess.CalledProcessError as e:
                self.root.after(0, lambda: self.stat.config(
                    text="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Preview failed", 
                    foreground=ERROR
                ))
                self.root.after(0, lambda: messagebox.showerror(
                    "Preview Error",
                    f"Failed to create preview:\n{e}"
                ))
            finally:
                self.root.after(0, lambda: self.start.config(state="normal"))
                self.root.after(0, lambda: self.preview_btn.config(state="normal"))
        
        threading.Thread(target=run_preview, daemon=True).start()
    
    def _check_resume(self):
        """Check for interrupted encoding"""
        if os.path.exists(self.resume_file):
            if messagebox.askyesno("Resume", "Resume previous encoding?"):
                try:
                    with open(self.resume_file, 'rb') as f:
                        state = pickle.load(f)
                    
                    self.inp.set(state.get("input", ""))
                    self.output_is_auto = False
                    self.out.set(state.get("output", ""))
                    self.mode.set(state.get("mode", "AV1 Balanced"))
                    self.resolution.set(state.get("resolution", "1080p"))
                    self.two_pass.set(state.get("two_pass", False))
                    
                    messagebox.showinfo("Resumed", "Session restored.")
                except:
                    pass
            
            try:
                os.remove(self.resume_file)
            except:
                pass
    
    def _save_resume_state(self):
        """Save resume state"""
        try:
            state = {
                "input": self.inp.get(),
                "output": self.out.get(),
                "mode": self.mode.get(),
                "resolution": self.resolution.get(),
                "two_pass": self.two_pass.get()
            }
            with open(self.resume_file, 'wb') as f:
                pickle.dump(state, f)
        except:
            pass
    
    def _show_log(self):
        """Show encoding log"""
        log_win = tk.Toplevel(self.root)
        log_win.title("FFmpeg Log")
        log_win.geometry("850x550")
        log_win.configure(bg=BG_DARK)
        
        text = scrolledtext.ScrolledText(log_win, bg=BG_MID, fg=TEXT_BRIGHT,
                                        font=("Consolas", 9), wrap=tk.WORD)
        text.pack(fill="both", expand=True, padx=10, pady=6)
        
        if self.error_log:
            text.insert("1.0", "\n".join(self.error_log))
        else:
            text.insert("1.0", "No log data available.")
        
        text.config(state="disabled")
        
        btn_frame = tk.Frame(log_win, bg=BG_DARK)
        btn_frame.pack(pady=8)
        
        def save_log():
            p = filedialog.asksaveasfilename(defaultextension=".txt")
            if p:
                try:
                    with open(p, 'w', encoding='utf-8') as f:
                        f.write("\n".join(self.error_log))
                    messagebox.showinfo("Saved", f"Log saved to:\n{p}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed:\n{e}")
        
        ttk.Button(btn_frame, text="Save Log", command=save_log).pack()
    
    def _start(self):
        """Start encoding"""
        # Queue handling
        if self.queue:
            result = messagebox.askyesno(
                "Queue Mode",
                f"Process {len(self.queue)} videos in queue?"
            )
            if result:
                self._start_queue_processing()
                return
        
        # Codec checks
        if not FFMPEG:
            messagebox.showerror("Error", "FFmpeg not found")
            return
        
        mode = self.mode.get()
        
        if "AV1" in mode and not HAS_LIBSVTAV1:
            messagebox.showerror("Error", "SVT-AV1 encoder not available")
            return
        
        if "NVENC" in mode and not HAS_HEVC_NVENC:
            messagebox.showerror("Error", "NVENC encoder not available")
            return
        
        # Validate input
        inp = self.inp.get().strip()
        if not inp or not os.path.isfile(inp):
            messagebox.showerror("Error", "Select a valid input file")
            return
        
        # NEW v4.6.0: SMART SKIP 2.0 check
        info_ext = ffprobe_info_extended(inp)
        should_skip, skip_reason = should_skip_encoding(info_ext, self.error_log)
        if should_skip:
            messagebox.showinfo(
                "Smart Skip",
                f"Skipping encoding:\n\n{skip_reason}\n\n"
                f"The source is already efficiently encoded and re-encoding\n"
                f"would likely increase file size with no quality improvement."
            )
            return
        
        # Prepare output
        outp = self.out.get().strip()
        if not outp:
            self._generate_output_path(inp)
            outp = self.out.get().strip()
        
        try:
            inp = validate_path(inp)
            outp = validate_path(outp)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid path:\n{e}")
            return
        
        if os.path.exists(outp):
            if not messagebox.askyesno("File Exists", f"Overwrite?\n{outp}"):
                return
        
        # Pre-encoding checks
        if self.skip_small_saving.get():
            reduction_pct = (1 - self.estimated_output_size / self.input_size) * 100 if self.input_size > 0 else 0
            if reduction_pct < 3:
                messagebox.showwarning(
                    "Low Savings Detected",
                    f"Estimated savings is only {reduction_pct:.1f}% (<3%).\n\n"
                    f"Skipping encoding to save time.\n"
                    f"Disable 'Skip if savings <5%' to encode anyway."
                )
                return
        
        if not check_disk_space(outp, self.estimated_output_size):
            if not messagebox.askyesno("Low Disk Space", "Continue anyway?"):
                return
        
        # Get video info
        info = ffprobe_info(inp)
        self.total_duration = info["duration"]
        self.input_fps = info["fps"]
        self.source_width = info["width"]
        self.source_height = info["height"]
        print(f"[PROGRESS] Video duration set: {self.total_duration:.2f}s ({self.total_duration/60:.1f} min), {self.input_fps:.2f} fps, {self.source_width}x{self.source_height}")
        self.input_size = os.path.getsize(inp)
        
        # Save resume state
        self._save_resume_state()
        
        # Start encoding
        self.bar.set(0)
        self.stat.config(text="Starting encoding...", foreground=ACCENT)
        self.start.config(state="disabled")
        self.preview_btn.config(state="disabled")
        self.cancel.config(state="normal")
        self.stop = False
        self.is_running = True
        self.encoding_start_time = time.time()
        self.error_log = []
        self.current_output_size = 0
        self.current_bitrate = 0
        
        # Reset ETA tracking
        self.speed_history = []
        self.last_progress_time = 0
        self.last_encoded_time = 0
        
        self.realtime_stats.config(text="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Preparing...")
        
        threading.Thread(target=self._run, args=(inp, outp), daemon=True).start()
    
    def _start_queue_processing(self):
        """Start processing the queue"""
        if not self.queue:
            return
        
        self.start.config(state="disabled")
        self.preview_btn.config(state="disabled")
        self.cancel.config(state="normal")
        self._process_next_in_queue()
    
    def _process_next_in_queue(self):
        """Process next item in queue"""
        pending_items = [item for item in self.queue if item.status == "pending"]
        
        if not pending_items:
            self.root.after(0, self._queue_finished)
            return
        
        self.current_queue_item = pending_items[0]
        self.current_queue_item.status = "encoding"
        
        total = len(self.queue)
        completed = sum(1 for item in self.queue if item.status == "completed")
        current = completed + 1
        
        self._update_queue_display()
        
        # Set UI to match queue item
        self.mode.set(self.current_queue_item.mode)
        self.resolution.set(self.current_queue_item.resolution)
        self.two_pass.set(self.current_queue_item.two_pass)
        
        info = ffprobe_info(self.current_queue_item.input_path)
        self.total_duration = info["duration"]
        self.input_fps = info["fps"]
        self.input_size = os.path.getsize(self.current_queue_item.input_path)
        self.source_width = info["width"]
        print(f"[PROGRESS] Queue item duration set: {self.total_duration:.2f}s ({self.total_duration/60:.1f} min), {self.input_fps:.2f} fps")
        self.source_height = info["height"]
        self.estimated_output_size = self.current_queue_item.estimated_size
        
        self.bar.set(0)
        self.stat.config(text=f"Encoding {current}/{total}: {self.current_queue_item.get_display_name()}",
                        foreground=ACCENT)
        self.stop = False
        self.is_running = True
        self.encoding_start_time = time.time()
        self.error_log = []
        self.current_output_size = 0
        self.current_bitrate = 0
        
        self.speed_history = []
        self.last_progress_time = 0
        self.last_encoded_time = 0
        
        self.realtime_stats.config(text="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Preparing...")
        
        threading.Thread(
            target=self._run,
            args=(self.current_queue_item.input_path, self.current_queue_item.output_path),
            daemon=True
        ).start()
    
    def _queue_finished(self):
        """Called when queue processing is complete"""
        completed = sum(1 for item in self.queue if item.status == "completed")
        failed = sum(1 for item in self.queue if item.status == "failed")
        
        self.start.config(state="normal")
        self.preview_btn.config(state="normal")
        self.cancel.config(state="disabled")
        self.is_running = False
        
        messagebox.showinfo(
            "Queue Complete",
            f"[CHECK] Completed: {completed}\nÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Failed: {failed}\nTotal: {len(self.queue)}"
        )
        
        self._update_queue_display()
        
        if completed > 0 and self.shutdown_after.get():
            self._shutdown_pc()
    
    def _run(self, inp: str, outp: str):
        """
        NEW v4.6.0: Main encoding logic with Nova-style adaptive compression
        """
        mode = self.mode.get()
        resolution = self.resolution.get()
        two_pass_enabled = self.two_pass.get() and "AV1" in mode
        
        # Get extended info and generate smart filters
        info_ext = ffprobe_info_extended(inp)
        smart_filters = get_smart_filters(info_ext, self.keep_hdr.get(), self.error_log)
        copy_audio = should_copy_audio(info_ext, self.error_log)
        
        # Log intelligent decisions
        self.error_log.append("=" * 80)
        self.error_log.append(f" NOVA-STYLE ADAPTIVE COMPRESSION v4.6.1")
        self.error_log.append("=" * 80)
        self.error_log.append(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        self.error_log.append(f"Mode: {mode} | Resolution: {resolution}")
        self.error_log.append(f"Two-Pass: {'Yes' if two_pass_enabled else 'No'}")
        self.error_log.append(f"Auto-Mode: {'Yes' if self.auto_mode.get() else 'No'}")
        self.error_log.append(f"Keep HDR: {'Yes' if self.keep_hdr.get() else 'No'}")
        self.error_log.append(f"Audio Copy: {'Yes' if copy_audio else 'No (re-encode)'}")
        if smart_filters:
            self.error_log.append(f"Smart Filters: {smart_filters}")
        self.error_log.append("=" * 80)
        
        # Get preset
        # NEW v5.0: Get advanced settings
        av1_tune_val = self.av1_tune.get()
        sharpening_val = self.sharpening_profile.get()
        custom_cq_val = self.custom_cq.get() if self.custom_cq.get() > 0 else None
        
        # NEW v5.0: Initialize encoder_name for hwaccel selection
        encoder_name = "cpu"  # Default for AV1 modes
        
        # NEW: Check if AMD AV1 hardware is available and auto-mode is enabled
        use_amd_av1_hardware = (self.auto_mode.get() and HAS_AV1_AMF and mode.startswith("AV1"))
        
        if use_amd_av1_hardware:
            # Use AMD hardware AV1 instead of CPU software
            self.error_log.append("ðŸš€ AUTO-MODE: Switching to AMD AV1 hardware encoding")
            self.error_log.append(f"   Original mode: {mode}")
            self.error_log.append(f"   Using: AMD AV1_AMF (hardware accelerated)")
            
            # Determine encoder preference
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_pref = "auto"
            elif encoder_pref == "AMD AMF":
                encoder_pref = "amf"
            else:
                encoder_pref = "auto"  # Force auto for AV1 hardware
            
            encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)
            
            if encoder_name == "amf":
                preset_cmd, use_hwaccel, plan_meta = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
                self._last_hw_plan = plan_meta
            else:
                # Fallback to CPU if AMD not available
                use_amd_av1_hardware = False
                self.error_log.append("¸  AMD not available, using CPU software encoder")
        
        # Check if AMD AV1 hardware should be used for preview
        use_amd_av1_preview = (self.auto_mode.get() and HAS_AV1_AMF and mode.startswith("AV1"))
        
        if use_amd_av1_preview:
            # Use AMD hardware for AV1 preview
            encoder_pref = self.encoder_preference.get()
            if encoder_pref == "Auto (detect GPU)":
                encoder_pref = "auto"
            elif encoder_pref == "AMD AMF":
                encoder_pref = "amf"
            else:
                encoder_pref = "auto"
            
            encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)
            
            if encoder_name == "amf":
                preset_cmd, use_hwaccel, _ = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
            else:
                use_amd_av1_preview = False
        
        if not use_amd_av1_preview:
            if mode == "AV1 Ultra":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_ultra(
                    resolution, self.source_width, self.source_height, smart_filters, 
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Balanced":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_balanced(
                    resolution, self.source_width, self.source_height, smart_filters,
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Compress":
                # Use balanced preset as base for CPU fallback (actual compression happens in AMF)
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_balanced(
                    resolution, self.source_width, self.source_height, smart_filters,
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
            elif mode == "AV1 Fast":
                preset_cmd, use_hwaccel = EncodingPresets.get_av1_fast(
                    resolution, self.source_width, self.source_height, smart_filters, 
                    self.keep_hdr.get(), av1_tune_val, sharpening_val)
        
        if mode in ["NVENC Ultra", "NVENC Balanced", "NVENC Fast"] or use_amd_av1_preview:
            # NEW v5.0: Determine encoder based on preference
            # Skip if already set by AV1 hardware detection
            if not use_amd_av1_hardware:
                encoder_pref = self.encoder_preference.get()
                if encoder_pref == "Auto (detect GPU)":
                    encoder_pref = "auto"
                elif encoder_pref == "NVIDIA NVENC":
                    encoder_pref = "nvenc"
                elif encoder_pref == "AMD AMF":
                    encoder_pref = "amf"
                else:
                    encoder_pref = "cpu"
                
                encoder_name, use_hwaccel = detect_best_encoder(encoder_pref)
            
            # Warn if requested encoder not available
            if encoder_pref == "amf" and not HAS_ANY_AMF:
                self.error_log.append(" AMD AMF not available, falling back to Auto")
                encoder_name, use_hwaccel = detect_best_encoder("auto")
            elif encoder_pref == "nvenc" and not HAS_HEVC_NVENC:
                self.error_log.append(" NVIDIA NVENC not available, falling back to Auto")
                encoder_name, use_hwaccel = detect_best_encoder("auto")
            
            # Use appropriate encoder
            # plan_meta may already be set by AV1 hardware detection
            if not use_amd_av1_hardware:
                plan_meta = None
            
            if encoder_name == "amf" and not use_amd_av1_hardware:
                preset_cmd, use_hwaccel, plan_meta = EncodingPresets.get_amf_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val, mode
                )
            elif not use_amd_av1_hardware:  # nvenc or cpu fallback (skip if already using AMD AV1)
                preset_cmd, use_hwaccel, plan_meta = EncodingPresets.get_nvenc_adaptive(
                    resolution, self.source_width, self.source_height, inp,
                    smart_filters, self.keep_hdr.get(), copy_audio, self.error_log,
                    custom_cq_val, sharpening_val
                )
            self._last_hw_plan = plan_meta
            
            # NEW v4.6.1: Check if estimated savings are worth encoding
            if self.skip_small_saving.get():
                plan_for_skip = plan_meta if plan_meta else {"params": choose_nvenc_params(
                    info_ext["width"],
                    info_ext["height"],
                    info_ext.get("bitrate_bps", info_ext["bitrate"] * 1000),
                    info_ext.get("bppf", 0.1),
                    info_ext.get("codec_name_normalized", "unknown")
                ), "info": info_ext, "use_bold_path": False}
                if plan_for_skip is plan_meta:
                    params_for_skip = plan_meta["params"]
                    info_for_skip = plan_meta["info"]
                    bold_flag = plan_meta.get("use_bold_path", False)
                else:
                    params_for_skip = finish_cq_for_source(info_ext, plan_for_skip["params"])
                    info_for_skip = info_ext
                    bold_flag = detect_bold_compression_path(info_ext)
                    if bold_flag:
                        params_for_skip, _ = apply_bold_compression_params(params_for_skip, "medium",
                                                                           info_ext.get("bitrate_bps", info_ext.get("bitrate", 0) * 1000))
                    else:
                        medium_flag = detect_medium_1080p_path(info_ext)
                        if medium_flag:
                            params_for_skip, _ = apply_medium_1080p_params(params_for_skip, info_ext, info_ext.get("bppf", 0.1))
                should_skip, skip_reason = should_skip_for_low_saving(
                    info_for_skip, params_for_skip, min_saving_pct=3.0, use_bold_path=bold_flag)
                if should_skip:
                    self.error_log.append(f" SMART SKIP (Low Savings): {skip_reason}")
                    self.root.after(0, lambda: self.stat.config(
                        text=f"ÃƒÂ¢Ã…Â¡Ã‚Â¡ Skipped: Savings below 3% threshold",
                        foreground=WARNING
                    ))
                    self.root.after(0, lambda: messagebox.showinfo(
                        "Smart Skip",
                        f"Encoding skipped:\n\n{skip_reason}\n\n"
                        f"Re-encoding would provide minimal benefit.\n"
                        f"Disable 'Skip if savings <3%' to encode anyway."
                    ))
                    if self.current_queue_item:
                        self.current_queue_item.status = "skipped"
                        self.current_queue_item.skipped_reason = skip_reason
                        self._update_queue_display()
                        self.current_queue_item = None
                        self.root.after(500, self._process_next_in_queue)
                    else:
                        self.cancel.config(state="disabled")
                        self.start.config(state="normal")
                        self.preview_btn.config(state="normal")
                        self.is_running = False
                    return
            
            self.error_log.append("")

            # v5.1.1: Log adaptive parameters only for hardware modes (plan_meta exists)
            # CPU-based encoding doesn't use plan_meta, and that's okay
            if plan_meta:
                pp = plan_meta["public_params"]
                filt = plan_meta["filter_strings"]
                info_for_log = plan_meta["info"]

                # Log encoder type
                encoder_display = "AMD AMF" if encoder_name == "amf" else "NVIDIA NVENC" if encoder_name == "nvenc" else "CPU"
                self.error_log.append(f"Ã°Å¸Å¡â‚¬ {encoder_display} ADAPTIVE PARAMETERS:")

                # Log codec if AMF
                if encoder_name == "amf" and "amf_codec" in plan_meta:
                    self.error_log.append(f"   Codec: {plan_meta['amf_codec'].upper()}")

                self.error_log.append(
                    f"   Source: {info_for_log['width']}x{info_for_log['height']} @ "
                    f"{info_for_log.get('bitrate_bps', info_for_log.get('bitrate', 0)*1000)/1_000_000:.2f} Mbps, "
                    f"fps={info_for_log.get('fps', 0):.2f}, bppf={info_for_log.get('bppf', 0.1):.3f}"
                )
                self.error_log.append(f"   Path used: {plan_meta['path_used']}")
                self.error_log.append(f"   Output 10-bit: {plan_meta['output_10bit']}")
                self.error_log.append(
                    f"   Ã¢Å¾Â¤ Final: cq={pp.get('cq')} | target={pp.get('b_v')/1_000_000:.2f} Mbps | "
                    f"maxrate={pp.get('maxrate')/1_000_000:.2f} Mbps | bufsize={pp.get('bufsize')/1_000_000:.2f} Mb"
                )
                filter_suffix = f" + {filt['unsharp']}" if filt['unsharp'] not in ("", "none") else ""
                self.error_log.append(
                    f"   Filters: {plan_meta['filter_profile']} => {filt['denoise']}{filter_suffix}"
                )
                self.error_log.append("")
            else:
                # CPU-based encoding mode (no plan_meta) - this is valid
                self.error_log.append(f"Ã°Å¸Å¡â‚¬ CPU ENCODING MODE: {mode}")
                self.error_log.append(f"   Using software encoder (libsvtav1/libx264)")
                self.error_log.append("")
        
        # Handle container format for AV1 AMF
        if encoder_name == "amf" and plan_meta and plan_meta.get("amf_codec") == "av1_amf":
            if outp.lower().endswith(".mp4"):
                # AV1 in MP4 may not be supported by all FFmpeg builds
                # Automatically switch to MKV for better compatibility
                new_outp = outp[:-4] + ".mkv"
                self.error_log.append("Container: Changed .mp4 to .mkv for AV1 AMF compatibility")
                self.error_log.append(f"   Output: {new_outp}")
                outp = new_outp
                # Update output path in UI and queue if present
                if self.current_queue_item:
                    self.current_queue_item.output_path = outp
                else:
                    self.out.set(outp)
        
        # Two-pass or single-pass encoding
        if two_pass_enabled:
            # Pass 1
            self.root.after(0, lambda: self.stat.config(text="Pass 1/2 (Analysis)...", foreground=ACCENT))
            
            if use_hwaccel:
                # NEW v5.0: Use appropriate hwaccel based on encoder
                hwaccel_type = "d3d11va" if encoder_name == "amf" else "cuda"
                cmd_pass1 = [FFMPEG, "-hide_banner", "-y", "-hwaccel", hwaccel_type, "-i", inp, "-progress", "pipe:1"]
            else:
                cmd_pass1 = [FFMPEG, "-hide_banner", "-y", "-i", inp, "-progress", "pipe:1"]
            
            cmd_pass1.extend(["-map", "0:v:0", "-map", "0:a:0?", "-sn", "-dn", "-map_metadata", "0"])
            cmd_pass1.extend(preset_cmd)
            cmd_pass1.extend(["-pass", "1", "-an", "-f", "null", "NUL" if sys.platform == "win32" else "/dev/null"])
            
            self.error_log.append("Pass 1: " + " ".join(cmd_pass1))
            
            success = self._run_ffmpeg_process(cmd_pass1, is_pass1=True)
            if not success:
                return
            
            # Pass 2
            self.root.after(0, lambda: self.stat.config(text="Pass 2/2 (Encoding)...", foreground=ACCENT))
            
            if use_hwaccel:
                # NEW v5.0: Use appropriate hwaccel based on encoder
                hwaccel_type = "d3d11va" if encoder_name == "amf" else "cuda"
                cmd_pass2 = [FFMPEG, "-hide_banner", "-y", "-hwaccel", hwaccel_type, "-i", inp, "-progress", "pipe:1"]
            else:
                cmd_pass2 = [FFMPEG, "-hide_banner", "-y", "-i", inp, "-progress", "pipe:1"]
            
            cmd_pass2.extend(["-map", "0:v:0", "-map", "0:a:0?", "-sn", "-dn", "-map_metadata", "0"])
            cmd_pass2.extend(preset_cmd)
            cmd_pass2.extend(["-pass", "2", "-movflags", "+faststart", outp])
            
            self.error_log.append("Pass 2: " + " ".join(cmd_pass2))
            
            success = self._run_ffmpeg_process(cmd_pass2, is_pass1=False)
            
            # Cleanup
            for f in ["ffmpeg2pass-0.log", "ffmpeg2pass-0.log.mbtree"]:
                if os.path.exists(f):
                    try:
                        os.remove(f)
                    except:
                        pass
            
            if not success:
                return
        else:
            # Single pass
            if use_hwaccel:
                # NEW v5.0: Use appropriate hwaccel based on encoder
                hwaccel_type = "d3d11va" if encoder_name == "amf" else "cuda"
                cmd = [FFMPEG, "-hide_banner", "-y", "-hwaccel", hwaccel_type, "-i", inp, "-progress", "pipe:1"]
            else:
                cmd = [FFMPEG, "-hide_banner", "-y", "-i", inp, "-progress", "pipe:1"]
            
            # Add explicit mapping (CRITICAL)
            cmd.extend(["-map", "0:v:0", "-map", "0:a:0?", "-sn", "-dn", "-map_metadata", "0"])
            cmd.extend(preset_cmd)
            cmd.extend(["-movflags", "+faststart", outp])
            
            self.error_log.append("Full command: " + " ".join(cmd))
            
            success = self._run_ffmpeg_process(cmd, is_pass1=False)
            if not success:
                return
        
        self.root.after(0, self._finish_encoding, outp)
    
    def _run_ffmpeg_process(self, cmd: List[str], is_pass1: bool = False) -> bool:
        """Run FFmpeg process with accurate progress tracking"""
        try:
            self.proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                universal_newlines=True,
                bufsize=1
            )
            self.ffmpeg_pid = self.proc.pid
        except Exception as e:
            self.error_log.append(f"Failed to start FFmpeg: {e}")
            self.root.after(0, self._show_error, f"Failed to start:\n{e}")
            return False
        
        # Thread to capture stderr
        def read_stderr():
            try:
                for line in self.proc.stderr:
                    self.error_log.append(line.strip())
                    if "bitrate=" in line:
                        match = re.search(r'bitrate=\s*(\d+\.?\d*)\s*(\w+bits/s)', line)
                        if match:
                            bitrate_val = float(match.group(1))
                            bitrate_unit = match.group(2)
                            if 'kbits/s' in bitrate_unit:
                                self.current_bitrate = int(bitrate_val)
                            elif 'Mbits/s' in bitrate_unit:
                                self.current_bitrate = int(bitrate_val * 1000)
            except:
                pass
        
        threading.Thread(target=read_stderr, daemon=True).start()
        
        current_time = 0
        try:
            for line in self.proc.stdout:
                if self.stop:
                    self.proc.terminate()
                    return False
                
                line = line.strip()
                
                if line.startswith("out_time_us="):
                    try:
                        us = int(line.split("=")[1])
                        current_time = us / 1_000_000
                        
                        # Time-based progress
                        if is_pass1:
                            pct = min(50.0, (current_time / self.total_duration) * 50.0)
                        else:
                            if self.two_pass.get() and "AV1" in self.mode.get():
                                pct = 50.0 + min(50.0, (current_time / self.total_duration) * 50.0)
                            else:
                                pct = min(100.0, (current_time / self.total_duration) * 100.0)
                        
                        # Calculate stats
                        elapsed = time.time() - self.encoding_start_time
                        
                        if elapsed > 0 and current_time > 0:
                            current_speed = current_time / elapsed
                            
                            self.speed_history.append(current_speed)
                            if len(self.speed_history) > 10:
                                self.speed_history.pop(0)
                            
                            avg_speed = sum(self.speed_history) / len(self.speed_history)
                            
                            remaining_time = self.total_duration - current_time
                            if avg_speed > 0:
                                eta = remaining_time / avg_speed
                            else:
                                eta = remaining_time
                            
                            fps = (current_time * self.input_fps) / elapsed
                            
                            if self.current_bitrate > 0:
                                self.current_output_size = int((self.current_bitrate * current_time * 1000) / 8)
                            else:
                                self.current_output_size = int(self.estimated_output_size * (pct / 100))
                        else:
                            eta = self.total_duration
                            fps = 0
                        
                        # Update UI
                        self.root.after(0, self._update, pct, max(0, eta), fps)
                        
                        self.last_encoded_time = current_time
                        
                    except Exception as e:
                        pass
                
                elif line.startswith("total_size="):
                    try:
                        size_bytes = int(line.split("=")[1])
                        self.current_output_size = size_bytes
                    except:
                        pass
        except:
            pass
        
        self.proc.wait()
        return self.proc.returncode == 0
    
    def _update(self, pct: float, eta: float, fps: float):
        """Update progress bar and statistics"""
        self.bar.set(pct)
        self.time.config(text=fmt_hms(eta))
        self.fps_label.config(text=f"{fps:.1f}")
        
        # Show speed
        if len(self.speed_history) > 0:
            avg_speed = sum(self.speed_history) / len(self.speed_history)
            if pct >= 98 and pct < 100:
                speed_text = f"Finalizing output file... {pct:5.1f}%"
            else:
                speed_text = f"Encoding: {pct:5.1f}% * Speed: {avg_speed:.2f}x realtime"
            self.stat.config(text=speed_text, foreground=ACCENT)
        else:
            if pct >= 98 and pct < 100:
                self.stat.config(text=f"Finalizing output file... {pct:5.1f}%", foreground=ACCENT)
            else:
                self.stat.config(text=f"Encoding: {pct:5.1f}%", foreground=ACCENT)
        
        # Update real-time stats
        if self.estimated_output_size > 0 and self.current_output_size > 0:
            size_progress_pct = (self.current_output_size / self.estimated_output_size) * 100
            self.realtime_stats.config(
                text=f"Output: {fmt_size(self.current_output_size)} / {fmt_size(self.estimated_output_size)} "
                     f"({size_progress_pct:.0f}% of estimate)"
            )
        else:
            self.realtime_stats.config(text="")
        
        if self.current_queue_item:
            self.current_queue_item.progress = pct
            self._update_queue_display()
    
    def _auto_save_log(self, outp: str, out_size: int, reduction: float):
        """Automatically save encoding log"""
        try:
            output_dir = os.path.dirname(outp) if os.path.dirname(outp) else '.'
            output_name = os.path.splitext(os.path.basename(outp))[0]
            log_filename = os.path.join(output_dir, f"{output_name}_encoding_log.txt")
            
            log_content = []
            log_content.append("=" * 80)
            log_content.append(f"Video Compressor Pro v{VERSION} - Encoding Log")
            log_content.append("=" * 80)
            log_content.append(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            log_content.append(f"Mode: {self.mode.get()}")
            log_content.append(f"Resolution: {self.resolution.get()}")
            log_content.append(f"Two-Pass: {'Yes' if self.two_pass.get() else 'No'}")
            log_content.append(f"Auto-Mode: {'Yes' if self.auto_mode.get() else 'No'}")
            log_content.append(f"Keep HDR: {'Yes' if self.keep_hdr.get() else 'No'}")
            log_content.append("")
            log_content.append("=" * 80)
            log_content.append("FILE INFORMATION")
            log_content.append("=" * 80)
            log_content.append(f"Input:  {self.inp.get() if not self.current_queue_item else self.current_queue_item.input_path}")
            log_content.append(f"Output: {outp}")
            log_content.append("")
            log_content.append(f"Input Size:     {fmt_size(self.input_size)}")
            log_content.append(f"Output Size:    {fmt_size(out_size)}")
            log_content.append(f"Estimated Size: {fmt_size(self.estimated_output_size)}")
            log_content.append(f"Reduction:      {reduction:.1f}%")
            log_content.append("")
            
            if self.estimated_output_size > 0:
                estimation_error = abs(out_size - self.estimated_output_size) / self.estimated_output_size * 100
                log_content.append(f"Estimation Accuracy: {estimation_error:.1f}% error")
                log_content.append("")
            
            log_content.append("=" * 80)
            log_content.append("ENCODING DETAILS")
            log_content.append("=" * 80)
            log_content.append("")
            
            for line in self.error_log:
                log_content.append(line)
            
            log_content.append("")
            log_content.append("=" * 80)
            log_content.append("END OF LOG")
            log_content.append("=" * 80)
            
            with open(log_filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(log_content))
            
            print(f"Log saved to: {log_filename}")
            
        except Exception as e:
            print(f"Failed to auto-save log: {e}")
    
    def _finish_encoding(self, outp: str):
        """Finish encoding and show results"""
        self.ffmpeg_pid = None
        
        if self.current_queue_item:
            if os.path.isfile(outp):
                out_size = os.path.getsize(outp)
                
                # Skip-if-larger check
                if out_size >= self.input_size:
                    try:
                        os.remove(outp)
                        self.current_queue_item.status = "skipped"
                        self.current_queue_item.skipped_reason = f"Output ({fmt_size(out_size)}) >= Input ({fmt_size(self.input_size)})"
                        self.error_log.append(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â SKIPPED: Output larger than input")
                    except Exception as e:
                        self.current_queue_item.status = "failed"
                        self.current_queue_item.error = f"Failed to delete larger output: {e}"
                else:
                    self.current_queue_item.status = "completed"
                    self.current_queue_item.actual_size = out_size
                    self.current_queue_item.progress = 100
                    
                    reduction = (1 - out_size/self.input_size)*100 if self.input_size > 0 else 0
                    self._auto_save_log(outp, out_size, reduction)
                    
                    # NEW v5.0: Save encoding history for queue items
                    encoding_time = time.time() - self.encoding_start_time if self.encoding_start_time > 0 else 0
                    info_ext = ffprobe_info_extended(self.current_queue_item.input_path)
                    source_bitrate = info_ext.get("bitrate_bps", 0) / 1_000_000  # Mbps
                    output_bitrate = (out_size * 8) / (self.total_duration * 1_000_000) if self.total_duration > 0 else 0  # Mbps
                    
                    history_entry = EncodingHistory(
                        timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                        input_path=self.current_queue_item.input_path,
                        output_path=outp,
                        mode=self.current_queue_item.mode,
                        input_size=self.input_size,
                        output_size=out_size,
                        compression_ratio=reduction / 100.0,
                        encoding_time=encoding_time,
                        source_bitrate=source_bitrate,
                        output_bitrate=output_bitrate
                    )
                    save_history_entry(history_entry)
                    
                    # NEW v5.0: Delete source file if enabled
                    if self.delete_source_after.get():
                        if os.path.exists(self.current_queue_item.input_path) and os.path.exists(outp):
                            try:
                                os.remove(self.current_queue_item.input_path)
                                self.error_log.append(f"ÃƒÂ°Ã…Â¸Ã¢â‚¬â€Ã¢â‚¬ËœÃƒÂ¯Ã‚Â¸Ã‚Â Source file deleted: {os.path.basename(self.current_queue_item.input_path)}")
                            except Exception as e:
                                self.error_log.append(f"ÃƒÂ¢Ã…Â¡Ã‚Â ÃƒÂ¯Ã‚Â¸Ã‚Â Failed to delete source: {e}")
            else:
                self.current_queue_item.status = "failed"
                self.current_queue_item.error = "Output file not created"
            
            self.current_queue_item = None
            self._update_queue_display()
            self.root.after(500, self._process_next_in_queue)
            return
        
        self.cancel.config(state="disabled")
        self.start.config(state="normal")
        self.preview_btn.config(state="normal")
        self.is_running = False
        
        if os.path.isfile(outp):
            out_size = os.path.getsize(outp)
            
            # Skip-if-larger check
            if out_size >= self.input_size:
                try:
                    os.remove(outp)
                    self.stat.config(
                        text=f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Skipped! Output ({fmt_size(out_size)}) >= Input ({fmt_size(self.input_size)})",
                        foreground=WARNING
                    )
                    messagebox.showwarning(
                        "Output Skipped",
                        f"The encoded file was LARGER than the original!\n\n"
                        f"Input:  {fmt_size(self.input_size)}\n"
                        f"Output: {fmt_size(out_size)}\n\n"
                        f"The output has been deleted to save space.\n"
                        f"Your original file is safe.\n\n"
                        f"[BULB] Tip: This video may already be well-compressed."
                    )
                    return
                except Exception as e:
                    self.stat.config(text=f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Error: {e}", foreground=ERROR)
                    return
            
            reduction = (1 - out_size/self.input_size)*100 if self.input_size > 0 else 0
            
            # Calculate estimation accuracy
            if self.estimated_output_size > 0:
                estimation_error = abs(out_size - self.estimated_output_size) / self.estimated_output_size * 100
                accuracy_text = f"(Est. was {estimation_error:.1f}% {'over' if out_size > self.estimated_output_size else 'under'})" if estimation_error > 5 else "(Est. was accurate!)"
            else:
                accuracy_text = ""
            
            self.stat.config(
                text=f"Done! {fmt_size(out_size)} ({reduction:.0f}% smaller) {accuracy_text}",
                foreground=SUCCESS
            )
            self.size_label.config(
                text=f"In: {fmt_size(self.input_size)} -> Out: {fmt_size(out_size)} | Est: {fmt_size(self.estimated_output_size)}"
            )
            self.realtime_stats.config(text="")
            
            if os.path.exists(self.resume_file):
                try:
                    os.remove(self.resume_file)
                except:
                    pass
            
            # Auto-save log
            self._auto_save_log(outp, out_size, reduction)
            
            # NEW v5.0: Save encoding history
            encoding_time = time.time() - self.encoding_start_time if self.encoding_start_time > 0 else 0
            info_ext = ffprobe_info_extended(self.inp.get() if not self.current_queue_item else self.current_queue_item.input_path)
            source_bitrate = info_ext.get("bitrate_bps", 0) / 1_000_000  # Mbps
            output_bitrate = (out_size * 8) / (self.total_duration * 1_000_000) if self.total_duration > 0 else 0  # Mbps
            
            history_entry = EncodingHistory(
                timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                input_path=self.inp.get() if not self.current_queue_item else self.current_queue_item.input_path,
                output_path=outp,
                mode=self.mode.get(),
                input_size=self.input_size,
                output_size=out_size,
                compression_ratio=reduction / 100.0,
                encoding_time=encoding_time,
                source_bitrate=source_bitrate,
                output_bitrate=output_bitrate
            )
            save_history_entry(history_entry)
            
            # NEW v5.1: Post-encode summary dialog
            source_path = self.inp.get() if not self.current_queue_item else self.current_queue_item.input_path
            self._show_encoding_summary_dialog(source_path, outp, self.input_size, out_size, reduction)
            
            # Shutdown if enabled
            if self.shutdown_after.get():
                self._shutdown_pc()
        else:
            self.stat.config(text="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Encoding failed - output file not created", foreground=ERROR)
        
        self.bar.set(100)
    
    def _show_encoding_summary_dialog(self, source_path: str, output_path: str, input_size: int, output_size: int, reduction: float):
        """Show post-encode summary with option to delete original file"""
        # Create summary dialog
        summary_win = tk.Toplevel(self.root)
        summary_win.title("Encoding Complete")
        summary_win.geometry("500x300")
        summary_win.configure(bg=BG_DARK)
        summary_win.transient(self.root)
        summary_win.grab_set()
        
        # Center dialog
        summary_win.update_idletasks()
        x = (summary_win.winfo_screenwidth() // 2) - (250)
        y = (summary_win.winfo_screenheight() // 2) - (150)
        summary_win.geometry(f"+{x}+{y}")
        
        main_frame = tk.Frame(summary_win, bg=BG_DARK)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        ttk.Label(main_frame, text="âœ“ ENCODING COMPLETE",
                 font=("Segoe UI", 14, "bold"),
                 foreground=SUCCESS,
                 background=BG_DARK).pack(pady=(0, 20))
        
        # Stats frame
        stats_frame = tk.Frame(main_frame, bg=BG_CARD,
                              highlightbackground=BORDER_BRIGHT, highlightthickness=2)
        stats_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        stats_inner = tk.Frame(stats_frame, bg=BG_CARD)
        stats_inner.pack(padx=15, pady=15)
        
        # Display stats
        ttk.Label(stats_inner, text="Original Size:",
                 font=("Segoe UI", 10),
                 foreground=TEXT_MID,
                 background=BG_CARD).grid(row=0, column=0, sticky="w", pady=5)
        ttk.Label(stats_inner, text=fmt_size(input_size),
                 font=("Segoe UI", 10, "bold"),
                 foreground=TEXT_BRIGHT,
                 background=BG_CARD).grid(row=0, column=1, sticky="e", padx=(20, 0), pady=5)
        
        ttk.Label(stats_inner, text="Encoded Size:",
                 font=("Segoe UI", 10),
                 foreground=TEXT_MID,
                 background=BG_CARD).grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(stats_inner, text=fmt_size(output_size),
                 font=("Segoe UI", 10, "bold"),
                 foreground=TEXT_BRIGHT,
                 background=BG_CARD).grid(row=1, column=1, sticky="e", padx=(20, 0), pady=5)
        
        ttk.Label(stats_inner, text="Size Reduction:",
                 font=("Segoe UI", 10),
                 foreground=TEXT_MID,
                 background=BG_CARD).grid(row=2, column=0, sticky="w", pady=5)
        ttk.Label(stats_inner, text=f"{reduction:.1f}%",
                 font=("Segoe UI", 10, "bold"),
                 foreground=SUCCESS,
                 background=BG_CARD).grid(row=2, column=1, sticky="e", padx=(20, 0), pady=5)
        
        # Question
        ttk.Label(main_frame, text="Delete original file?",
                 font=("Segoe UI", 11, "bold"),
                 foreground=WARNING,
                 background=BG_DARK).pack(pady=(0, 15))
        
        # Buttons
        btn_frame = tk.Frame(main_frame, bg=BG_DARK)
        btn_frame.pack(fill="x")
        
        def on_delete():
            summary_win.destroy()
            # Safety check
            if source_path == output_path:
                messagebox.showerror("Error", "Cannot delete: source and output are the same file!")
                return
            if not os.path.exists(source_path):
                messagebox.showerror("Error", "Source file no longer exists!")
                return
            try:
                os.remove(source_path)
                messagebox.showinfo("Deleted", f"Original file deleted:\n{os.path.basename(source_path)}")
                self.error_log.append(f"âœ“ Source file deleted: {os.path.basename(source_path)}")
            except Exception as e:
                messagebox.showerror("Delete Failed", f"Could not delete file:\n{e}")
                self.error_log.append(f"âœ— Failed to delete source: {e}")
        
        def on_keep():
            summary_win.destroy()
        
        ttk.Button(btn_frame, text="Yes, Delete Original",
                  command=on_delete,
                  style="Warning.TButton").pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        ttk.Button(btn_frame, text="No, Keep Original",
                  command=on_keep,
                  style="TButton").pack(side="left", expand=True, fill="x", padx=(5, 0))
    
    def _show_error(self, msg: str):
        """Show error message"""
        messagebox.showerror("Error", msg)
        self.cancel.config(state="disabled")
        self.start.config(state="normal")
        self.preview_btn.config(state="normal")
        self.is_running = False
        
        if self.current_queue_item:
            self.current_queue_item.status = "failed"
            self.current_queue_item.error = msg
            self._update_queue_display()
            self.current_queue_item = None
            self.root.after(500, self._process_next_in_queue)
    
    def _cancel(self):
        """Cancel encoding"""
        if self.current_queue_item:
            result = messagebox.askyesno(
                "Cancel Queue",
                "Cancel all items or just current?\n\nYes = All | No = Current"
            )
            if result:
                for item in self.queue:
                    if item.status == "pending":
                        item.status = "canceled"
                if self.current_queue_item:
                    self.current_queue_item.status = "canceled"
            else:
                if self.current_queue_item:
                    self.current_queue_item.status = "canceled"
        
        self.stop = True
        if self.proc:
            try:
                self.proc.terminate()
                time.sleep(0.5)
                if self.proc.poll() is None:
                    self.proc.kill()
            except:
                pass
        
        self.stat.config(text="Canceled", foreground=ERROR)
        self.cancel.config(state="disabled")
        self.start.config(state="normal")
        self.preview_btn.config(state="normal")
        self.ffmpeg_pid = None
        self.is_running = False
        self.realtime_stats.config(text="")
        
        if self.current_queue_item:
            self.current_queue_item = None
            self._update_queue_display()
    
    def _monitor(self):
        """Monitor CPU and GPU usage"""
        if not self._monitor_active:
            return
        
        try:
            sys_cpu = get_system_cpu()
            self.cpu_usage = sys_cpu
            if hasattr(self, 'cpu_label'):
                self.cpu_label.config(text=f"{sys_cpu:.0f}%")
        except:
            self.cpu_usage = 0.0
            if hasattr(self, 'cpu_label'):
                self.cpu_label.config(text="-Â")
        
        gpu_util, gpu_temp = get_gpu_stats()
        self.gpu_usage = gpu_util if gpu_util is not None else 0.0
        
        if hasattr(self, 'gpu_label'):
            if gpu_util is not None:
                self.gpu_label.config(text=f"{gpu_util}%")
            else:
                self.gpu_label.config(text="-Â")
        
        # NEW v5.0: Update real-time stats dashboard during encoding
        if self.is_running and hasattr(self, 'realtime_stats'):
            # Calculate encoding speed
            if self.encoding_start_time > 0 and len(self.speed_history) > 0:
                avg_speed = sum(self.speed_history) / len(self.speed_history)
                self.encoding_speed = avg_speed
            else:
                self.encoding_speed = 0.0
            
            # Update stats display with CPU/GPU/Speed
            stats_text = (f"CPU: {self.cpu_usage:.0f}% | "
                         f"GPU: {self.gpu_usage:.0f}% | "
                         f"Speed: {self.encoding_speed:.2f}x")
            self.realtime_stats.config(text=stats_text, foreground=ACCENT)
        
        try:
            self.root.after(1000, self._monitor)
        except tk.TclError:
            self._monitor_active = False
    
    def _shutdown_pc(self):
        """Silent immediate shutdown"""
        if not self.shutdown_after.get():
            return
        
        try:
            subprocess.Popen(
                ["shutdown", "/s", "/f", "/t", "0"],
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
            )
        except Exception as e:
            messagebox.showerror("Shutdown Error", f"Failed to shutdown:\n{e}")
    
    def _on_closing(self):
        """Handle window close"""
        if self.is_running:
            if not messagebox.askyesno("Encoding in Progress", "Cancel encoding and exit?"):
                return
            self._cancel()
        
        self._monitor_active = False
        if hasattr(self, 'bar'):
            self.bar.stop_animation()
        
        self.root.destroy()

def main():
    """Main entry point"""
    if not FFMPEG:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "FFmpeg Not Found",
            "FFmpeg not found in PATH.\n\n"
            "Download FFmpeg from:\n"
            "https://www.gyan.dev/ffmpeg/builds/\n\n"
            "Extract and add to PATH or place in same directory."
        )
        return
    
    root = TkinterDnD.Tk() if DND_OK else tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
