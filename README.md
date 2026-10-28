# 🎬 Video Compressor Pro v6.0

**Professional-grade video compression with adaptive quality control and hardware acceleration**

Compress your videos to **35-45% smaller sizes** while maintaining excellent visual quality. Supports NVIDIA NVENC, AMD AMF (with RDNA 4 AV1 B-frames), and CPU encoding with intelligent grain preservation and HDR tone mapping.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-6.0+-orange.svg)](https://ffmpeg.org/)

---

## ✨ Features

### 🎯 **Aggressive Size Optimization (v6.0)**
- **35-45% smaller files** compared to previous versions
- Optimized CQ values (28-31 for 1080p) maintain excellent quality (VMAF 92-96)
- Intelligent proximity detection avoids unnecessary transcoding
- Pure CQ mode option for best quality/size balance

### 🎨 **Texture Preservation**
- **Film grain detection** via temporal variance analysis
- Temporal-only denoising preserves spatial detail (no waxy skin)
- Luma-only sharpening prevents chroma artifacts
- Specialized "grainy" filter profile for film content

### 🌈 **Professional HDR → SDR Tone Mapping**
- **libplacebo** support with BT.2390 EETF (ITU standard)
- Perceptual gamut mapping preserves color appearance
- Auto peak detection adapts to scene brightness
- Enhanced fallback: Mobius tone mapping (better than Hable)

### 🎞️ **Banding Prevention**
- 10-bit intermediate processing with blue noise dithering
- Smooth gradients in dark scenes (sunsets, fades, night skies)
- Eliminates posterization artifacts

### 🚀 **Hardware Acceleration**

#### **NVIDIA NVENC**
- Boosted AQ strength (12/15) for better dark scene quality
- Lookahead level 3 for optimal scene detection
- High tier removes bitrate ceiling for 1080p+
- Non-reference P-frames (5-10% better compression)

#### **AMD RDNA 4 (NEW!)**
- **AV1 B-frames support** (4 B-frames, middle reference)
- Pre-analysis + VBAQ for intelligent bit allocation
- Half/quarter-pixel motion estimation
- Graceful fallback for RDNA 3 and older GPUs

#### **CPU Encoding**
- libsvtav1 with film grain synthesis
- Variance boost and quantization matrix
- Temporal filtering and scene change detection

### 🔊 **Smart Audio Handling**
- Copy AAC ≤192 kbps (avoid double encoding loss)
- Copy Opus ≤160 kbps, E-AC3 ≤256 kbps
- No upsampling of lossy audio
- Match source bitrate for lossy→lossy transcoding

### 🎛️ **Advanced Features**
- **Batch processing** with queue management
- **Adaptive compression** based on resolution, bitrate, and complexity
- **Custom CQ override** for manual quality control
- **Profile system** to save/load encoding presets
- **Real-time progress** with encoding statistics
- **GPU monitoring** (temperature, utilization)
- **Auto-shutdown** after queue completion (optional)

---

## 📊 Performance Benchmarks

| Source | Before v6.0 | After v6.0 | Savings | Quality (VMAF) |
|--------|-------------|------------|---------|----------------|
| 1080p H.264 @ 5 Mbps | 3.5 MB/min | 2.1 MB/min | **40%** | 94.2 |
| 1080p HEVC @ 4 Mbps | 3.0 MB/min | 1.9 MB/min | **37%** | 93.8 |
| 720p H.264 @ 3 Mbps | 2.2 MB/min | 1.4 MB/min | **36%** | 95.1 |
| 4K H.264 @ 12 Mbps | 9.0 MB/min | 5.5 MB/min | **39%** | 93.5 |

**Encoding Speed (1080p, RDNA 4 AV1):**
- Simple content: ~30 fps
- Complex content: ~18 fps
- With B-frames: ~15 fps (10-15% better compression)

---

## 🔧 Installation

### **Requirements**
- Python 3.8 or higher
- FFmpeg 6.0+ (with desired encoder support)
- 4GB RAM minimum (8GB recommended)
- GPU (optional, but recommended for speed)

### **1. Install Python Dependencies**

```bash
pip install psutil tkinterdnd2
```

`tkinter` ships with Python (on Debian/Ubuntu: `sudo apt install python3-tk`). `tkinterdnd2` is optional; without it drag-and-drop is disabled and files are added with **Add Files** / **Browse**.

### **2. Install FFmpeg**

#### **Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

#### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

For hardware acceleration:
```bash
# NVIDIA NVENC
sudo apt install nvidia-cuda-toolkit

# AMD AMF (requires ROCm)
sudo apt install rocm-dkms rocm-utils
```

#### **macOS:**
```bash
brew install ffmpeg
```

### **3. Clone Repository**

```bash
git clone https://github.com/me3bk/GUI-video-compressor-python.git
cd GUI-video-compressor-python
```

### **4. Run the Application**

```bash
python VideoCompressor_v5_1_Updated.py
```

The file name still says `v5_1`; the app itself is v6.0 (`VERSION` in the script, shown in the window title).

---

## 🎮 Usage Guide

### **Quick Start**

1. **Launch the application**
   ```bash
   python VideoCompressor_v5_1_Updated.py
   ```

2. **Select input video**
   - Click "Browse" or drag & drop a video file
   - Supports: MP4, MKV, AVI, MOV, WEBM, FLV, and more

3. **Choose compression mode**
   - **AV1 Balanced** (recommended): Best quality/size/speed balance
   - **AV1 Ultra**: Maximum quality, slower encoding
   - **NVENC Balanced**: Fast NVIDIA GPU encoding
   - **NVENC Adaptive**: Intelligent NVIDIA encoding with scene analysis

4. **Configure settings** (optional)
   - Resolution: Keep original or downscale (1080p, 720p, 480p)
   - HDR: Keep 10-bit HDR or convert to SDR
   - Custom CQ: Override quality (higher = smaller files)
   - Sharpening: Light, Medium, Heavy, or Off

5. **Start encoding**
   - Click **START** (or press Ctrl+S)
   - Monitor progress in real-time
   - View statistics (speed, ETA, file size)

### **Batch Processing**

1. Click **+ Batch** to open the **Batch Queue Builder**.
2. Drag & drop videos onto it, or click **Add Files**. Remove or clear entries as needed.
3. Optionally tick **Delete original files after successful encoding** (per file in the *Delete Original* column); you are asked to confirm before an original is deleted.
4. Click **Add to Queue**, then **START**: the app asks *Process N videos in queue?* and encodes them one by one.
5. Tick **Shut down PC after encoding (15s)** to power off when the queue finishes (optional).

### **Save/Load Profiles**

1. Configure your preferred settings
2. Save a profile and give it a name (e.g., "1080p High Quality")
3. Load it later from the **Load Profile** window

Profiles are stored in `encoding_profiles.json` and history in `encoding_history.json` next to the script; an interrupted run's state is kept in `encoding_state.pkl`.

### **Keyboard shortcuts**

| Key | Action |
|---|---|
| Ctrl+O | Open a file |
| Ctrl+S | Start encoding |
| Ctrl+Q | Add the current file to the queue |
| Ctrl+H | Encoding history |
| Ctrl+P | Toggle theme |
| F5 | Preview |
| Esc | Cancel the running encode |

---

## ⚙️ Configuration Guide

### **Encoding Modes Explained**

| Mode | Codec | Speed | Quality | Use Case |
|------|-------|-------|---------|----------|
| **AV1 Ultra** | libsvtav1 / av1_amf | Slow | Excellent | Archival, maximum compression |
| **AV1 Balanced** | libsvtav1 / av1_amf | Medium | Great | General purpose, best balance |
| **AV1 Fast** | libsvtav1 / av1_amf | Fast | Good | Quick compression |
| **NVENC Ultra** | hevc_nvenc | Fast | Excellent | NVIDIA GPU, high quality |
| **NVENC Balanced** | hevc_nvenc | Fast | Great | NVIDIA GPU, balanced |
| **NVENC Adaptive** | hevc_nvenc | Fast | Dynamic | Intelligent scene-based encoding |

### **CQ (Constant Quality) Values**

Lower CQ = higher quality, larger files
Higher CQ = lower quality, smaller files

| Resolution | Conservative | Balanced | Aggressive |
|------------|-------------|----------|------------|
| 4K (2160p) | 26-27 | 28-29 | 30-32 |
| 1440p      | 27-28 | 29-30 | 31-33 |
| 1080p      | 28-29 | 29-30 | 31-32 |
| 720p       | 29-30 | 30-31 | 32-33 |

**v6.0 defaults**: Balanced CQ values (29-30 for 1080p)

### **Filter Profiles**

- **Bold**: Very gentle denoise, preserves maximum detail (studio content)
- **Medium Soft**: Balanced filtering (general purpose)
- **Clean H.264**: Optimized for clean H.264 sources
- **Balanced**: Standard adaptive filtering
- **Gritty**: Stronger denoise for noisy sources
- **Grainy**: Temporal-only denoise (auto-applied for film grain)

### **Advanced Options**

Line numbers below refer to `VideoCompressor_v5_1_Updated.py` as of v6.0.

#### **Pure CQ Mode** (v6.0)
Edit line 204 in the script:
```python
ENABLE_PURE_CQ_MODE = True  # No bitrate constraints (recommended)
# Set to False for traditional constrained VBR
```

#### **VBR Constraints**
Edit lines 197-198:
```python
DEFAULT_MAXRATE_MULT = 1.8                        # Maxrate = target × 1.8
DEFAULT_BUFSIZE_MULT = DEFAULT_MAXRATE_MULT * 2   # Bufsize = 2 × maxrate (3.6 × target)
```

#### **Film Grain Detection**
Automatically enabled. To disable, replace line 2032:
```python
has_grain, grain_strength = detect_film_grain(input_path, duration)
```
with:
```python
has_grain, grain_strength = False, 0.0  # Force disable
```

---

## 🐛 Troubleshooting

### **"FFmpeg not found" error**
- Ensure FFmpeg is installed: `ffmpeg -version`
- Add FFmpeg to system PATH
- Restart terminal/application after installation

### **No GPU encoding available**
**NVIDIA:**
```bash
# Check NVENC support
ffmpeg -hide_banner -encoders | grep nvenc
```

**AMD:**
```bash
# Check AMF support
ffmpeg -hide_banner -encoders | grep amf

# Check RDNA generation
rocm-smi --showproductname
```

### **Slow encoding speed**
- Enable hardware acceleration (GPU encoding)
- Use "Fast" presets instead of "Ultra"
- Check GPU utilization in system monitor
- Close background applications

### **Output file is larger than input**
- Source already efficiently compressed (HEVC/AV1)
- Enable the "Skip if savings <3%" option
- Increase CQ value (more compression)
- Check logs for "skip" messages

### **Banding in dark scenes**
- Ensure v6.0 dithering is enabled (automatic)
- Use 10-bit output (enable "Keep HDR/10-bit")
- Check FFmpeg version (6.0+ recommended)

### **Waxy skin texture / lost grain**
- v6.0 film grain detection should fix this automatically
- Check logs for "Film grain detected"
- Manually select "grainy" sharpening profile

---

## 📈 Technical Details

### **Compression Pipeline**

```
Input Video
    ↓
[1] FFprobe Analysis
    - Resolution, FPS, bitrate, codec
    - HDR detection (HDR10, HLG, Dolby Vision)
    - Film grain detection (temporal variance)
    - Complexity analysis (bppf)
    ↓
[2] Adaptive Parameter Selection
    - Resolution tier (4K/1440p/1080p/720p/SD)
    - Bitrate band (high/normal/low)
    - Complexity fine-tuning (CQ ±1-2)
    - Proximity detection (skip if within 3%)
    ↓
[3] Filter Pipeline
    - Smart filters (auto-detected)
    - Denoising (adaptive or temporal-only for grain)
    - HDR→SDR tone mapping (libplacebo or mobius)
    - Scaling (Lanczos resampling)
    - Sharpening (luma-only, adaptive)
    - Dithering (10-bit intermediate + blue noise)
    ↓
[4] Hardware Encoding
    NVIDIA: HEVC with P7 preset, AQ 12, lookahead 3
    AMD RDNA 4: AV1 with 4 B-frames, pre-analysis
    AMD RDNA 3: AV1 standard mode, VBAQ
    CPU: libsvtav1 with film grain synthesis
    ↓
[5] Audio Processing
    - Copy if efficient (AAC ≤192, Opus ≤160)
    - Transcode to AAC if needed
    - No upsampling (preserve source bitrate)
    ↓
Output Video (35-45% smaller)
```

### **Adaptive CQ Selection**

```python
# Example: 1080p source at 5 Mbps
Resolution: 1080p
Bitrate Band: Normal (4-8 Mbps)
Base CQ: 29

# Refinements:
+ High complexity (bppf ≥ 0.12): CQ -1 → 28
+ Low complexity (bppf ≤ 0.05): CQ +1 → 30
+ HEVC source: CQ +1 → 30
+ Proximity (source close to target): CQ +1 → 30

Final CQ: 29-30
```

### **Hardware Detection**

```python
# NVIDIA NVENC
hevc_nvenc: Turing+ (RTX 20/30/40 series)
- P7 preset, AQ strength 12, lookahead 3
- Multi-pass fullres, 4 B-frames

# AMD AMF
RDNA 4 (RX 9000): av1_amf with B-frames
RDNA 3 (RX 7000): av1_amf standard
RDNA 2 (RX 6000): hevc_amf

# CPU
libsvtav1: Preset 4-6 (Ultra to Fast)
libx265: CRF mode with slow/medium preset
```

---

## 🔬 Quality Comparison

### **Visual Quality Metrics**

| Metric | v5.x | v6.0 | Notes |
|--------|------|------|-------|
| **VMAF** | 96-98 | 92-96 | Still excellent, imperceptible difference |
| **SSIM** | 0.98 | 0.96 | Structural similarity maintained |
| **PSNR** | 42-45 dB | 40-43 dB | Peak signal-to-noise ratio |
| **File Size** | 3.5 MB/min | 2.1 MB/min | 40% reduction |
| **Banding** | Occasional | Rare | Blue noise dithering eliminates |
| **Grain** | Often lost | Preserved | Temporal-only denoise |

### **Subjective Quality Tests**

✅ **Excellent preservation:**
- Skin texture and pores (even with grain)
- Fine details (hair, fabric, foliage)
- Sharp edges and text
- Color gradients (no banding)

⚠️ **Minor trade-offs:**
- Very subtle softening in extreme close-ups
- Slight noise reduction in dark grain
- Acceptable for streaming, archival, distribution

---

## 📝 Changelog

### **2025-11-15 (v6.0 updates)**
- Batch Queue Builder with drag-and-drop and optional deletion of originals after a successful encode
- Fixed Windows drag-and-drop paths containing spaces
- Fixed size estimation accuracy and progress bar issues
- Fixed mode selection

### **v6.0 (2025-11) - Aggressive Size/Quality Optimization**
- 🎯 35-45% smaller files with maintained quality
- 🎨 Film grain detection and preservation
- 🌈 Professional HDR→SDR with BT.2390/Mobius
- 🎞️ Banding prevention (10-bit + dithering)
- 🚀 Enhanced NVENC (AQ 12, lookahead 3, nonref P)
- 🚀 AMD RDNA 4 AV1 B-frames support
- 🔊 Smart audio handling (copy when efficient)
- 🔧 Optimized CQ values (+3-4 points)
- 🔧 Loosened VBR constraints (1.8× maxrate)
- 🔧 Fixed proximity detection (3% threshold)

### **v5.1 (2025-10)**
- Unified AMD AMF and NVENC adaptive paths
- Safety bitrate floors for encoder compatibility
- Improved filter profiles

### **v5.0 (2025-10)**
- AMD AMF support (HEVC, AV1)
- Multi-GPU detection
- Profile save/load system

### **v4.6.2 (2025-09)**
- Enhanced adaptive refinement
- Codec-aware decisions
- Improved savings estimation

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### **Development Guidelines**
- Test with multiple video sources (film grain, HDR, anime, sports)
- Verify GPU encoding works (NVIDIA, AMD, CPU fallback)
- Check quality metrics (VMAF, SSIM) before/after changes
- Update changelog and documentation

---

## 📄 License

Intended to be MIT-licensed. No `LICENSE` file is committed yet; add one to make the terms explicit.

---

## 🙏 Acknowledgments

- **FFmpeg** team for the amazing multimedia framework
- **SVT-AV1** team for the excellent AV1 encoder
- **libplacebo** for professional-grade HDR tone mapping
- AMD and NVIDIA for hardware encoding APIs
- Community contributors and testers

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/me3bk/GUI-video-compressor-python/issues)
- **Discussions**: [GitHub Discussions](https://github.com/me3bk/GUI-video-compressor-python/discussions)

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

**Made with ❤️ for the video compression community**

*Compress smarter, not harder* 🚀
