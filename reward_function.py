import math
def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle'])
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    reward = 1e-3
    
    # Keep to center
    if distance_from_center <= (0.10 * track_width):
        reward += 1.0
    elif distance_from_center <= (0.25 * track_width):
        reward += 0.50
    elif distance_from_center <= (0.50 * track_width):
        reward += 0.05
    else:
        reward = 1e-3

    # Wheels on track & Speed
    if not all_wheels_on_track:
        reward -= 0.50
    elif speed < 1.5:
        reward -= 0.25
    else:
        reward += 0.75

    # Steering
    if abs_steering > 14:
        reward *= 0.75

    # Waypoints
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    if direction_diff > 10.0:
        reward *= 0.5

    return float(reward)
