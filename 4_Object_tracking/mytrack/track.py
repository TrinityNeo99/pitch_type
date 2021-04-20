import sys
sys.path.append("..")
from fmo_detection import detect_ball, plot_trajectory, plot_trajectory_on_video

input_path = "/Users/neotrinity/Downloads/test-pingpang-track/ping-pang-2.mov"
output_path = "/Users/neotrinity/Downloads/"

min_area = 40

ball_trajectory, _, _ = detect_ball(input_path, joints_array = None, plotting=False, min_area= min_area) #400
plot_trajectory_on_video(input_path, output_path+"test.mp4", ball_trajectory)