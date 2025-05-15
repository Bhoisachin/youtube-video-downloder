
import streamlit as st
import yt_dlp
import os

# Streamlit app title
st.title("Simple YouTube Video Downloader")

# Trademark notice
st.markdown("© 2025 StreamDownloader. All rights reserved.")

# Input field for YouTube URL
url = st.text_input("Enter YouTube Video URL:")

# Download button
if st.button("Download"):
    if url:
        try:
            # Configure yt_dlp options
            ydl_opts = {'format':'best','outtmpl':'%(title)s.%(ext)s'}
            
            # Download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info['title']
                video_file = f"downloads/{video_title}.mp4"
                
                st.write(f"Downloaded: {video_title}")
                
                # Offer the file for download via browser
                with open(video_file, "rb") as file:
                    st.download_button(
                        label="Download Video",
                        data=file,
                        file_name=f"{video_title}.mp4",
                        mime="video/mp4"
                    )
                
                st.success("Video ready! Click the button above to download it to your device.")
                
                # Optional: Clean up the temporary file (comment out to keep files in downloads folder)
                os.remove(video_file)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube URL.")