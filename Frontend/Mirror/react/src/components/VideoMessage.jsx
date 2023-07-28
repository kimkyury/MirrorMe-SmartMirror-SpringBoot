import React, { useState, useEffect, useRef } from 'react';

function VideoMessage(props) {
  const [user, setUser] = useState('123');
  const [playlist, setPlaylist] = useState([]); // 메세지 재생목록
  const [currentVideoIndex, setCurrentVideoIndex] = useState(0); // 현재 재생 인덱스

  // ref를 사용하여 video 요소 가져오기
  const videoRef = useRef(null);

  // 메세지 재생목록 업데이트
  const fetchPlaylist = () => {
    const tempPlaylist = [
      "video/video1.mp4",
      "video/video2.mp4",
      "video/video3.mp4",
      // 수정 예정
    ];
    setPlaylist(tempPlaylist);
  };

  // 컴포넌트 마운트 시 메세지 재생목록 업데이트
  useEffect(() => {
    fetchPlaylist();
  }, []);

  // 이전 메세지 재생
  const playPreviousVideo = () => {
    if (currentVideoIndex > 0) {
      setCurrentVideoIndex((prevIndex) => prevIndex - 1);
      if (videoRef.current) {
        videoRef.current.pause(); // 이전 메세지로 이동 시 일시 정지
        videoRef.current.load();
        videoRef.current.play(); // 이전 메세지 재생
      }
    } else {
      alert("이전 메세지가 없습니다.");
    }
  };

  // 다음 메세지 재생
  const playNextVideo = () => {
    if (currentVideoIndex < playlist.length - 1) {
      setCurrentVideoIndex((prevIndex) => prevIndex + 1);
      if (videoRef.current) {
        videoRef.current.pause(); // 다음 메세지로 이동 시 일시 정지
        videoRef.current.load();
        videoRef.current.play(); // 다음 메세지 재생
      }
    } else {
      alert("다음 메세지가 없습니다.");
    }
  };

  return (
    <div className="video">
      <h3>{user}님의 메세지</h3> {/* 추후 보낸 사람으로 수정 */}
      <hr />
      <video ref={videoRef} controls>
        <source src={playlist[currentVideoIndex]} type="video/mp4" />
      </video>
      <button onClick={playPreviousVideo}>이전 메세지</button>
      <button onClick={playNextVideo}>다음 메세지</button>
    </div>
  );
}

export default VideoMessage;
