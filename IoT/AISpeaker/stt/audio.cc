#include <alsa/asoundlib.h>
#include <iostream>
#include <vector>
#include <fstream>

int main() {
    // Open the PCM device for capture (마이크를 캡처하기 위해 PCM 장치를 엽니다)
    snd_pcm_t* capture_handle;
    if (snd_pcm_open(&capture_handle, "default", SND_PCM_STREAM_CAPTURE, 0) < 0) {
        std::cerr << "Error opening PCM device." << std::endl;
        return -1;
    }

    // Set the capture parameters (캡처 파라미터 설정)
    snd_pcm_hw_params_t* params;
    if (snd_pcm_hw_params_malloc(&params) < 0) {
        std::cerr << "Error allocating hardware parameter structure." << std::endl;
        return -1;
    }

    if (snd_pcm_hw_params_any(capture_handle, params) < 0) {
        std::cerr << "Error initializing hardware parameter structure." << std::endl;
        return -1;
    }

    if (snd_pcm_hw_params_set_access(capture_handle, params, SND_PCM_ACCESS_RW_INTERLEAVED) < 0) {
        std::cerr << "Error setting access type." << std::endl;
        return -1;
    }

    unsigned int rate = 16000;
    if (snd_pcm_hw_params_set_rate_near(capture_handle, params, &rate, 0) < 0) {
        std::cerr << "Error setting sample rate." << std::endl;
        return -1;
    }

    if (snd_pcm_hw_params_set_channels(capture_handle, params, 1) < 0) {
        std::cerr << "Error setting channel count." << std::endl;
        return -1;
    }

    // Apply the capture parameters (캡처 파라미터 적용)
    if (snd_pcm_hw_params(capture_handle, params) < 0) {
        std::cerr << "Error setting hardware parameters." << std::endl;
        return -1;
    }

    snd_pcm_hw_params_free(params);

    // Allocate a buffer to hold the captured data (캡처된 데이터를 저장할 버퍼 할당)
    const int buffer_size = rate * 10;
    std::vector<short> buffer(buffer_size);

    // Capture audio from the microphone (마이크로부터 오디오 캡처)
    unsigned int frames_captured = 0;
    while (frames_captured < buffer.size()) {
        int num_frames = snd_pcm_readi(capture_handle, buffer.data(), buffer.size());
        if (num_frames < 0) {
            std::cerr << "Error reading from PCM device." << std::endl;
            break;
        }

	frames_captured += num_frames;
    }

    // Close the PCM device (PCM 장치 닫기)
    snd_pcm_close(capture_handle);
    
    // Save the captured audio to a file (캡처된 오디오를 파일로 저장)
    std::ofstream outfile("captured_audio.pcm", std::ios::binary);
    if (outfile) {
        outfile.write(reinterpret_cast<const char*>(buffer.data()), frames_captured * sizeof(short));
        outfile.close();
    } else {
        std::cerr << "Error saving captured audio to file." << std::endl;
    }
    
    
    return 0;
}

