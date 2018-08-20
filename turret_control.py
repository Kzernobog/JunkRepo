import queue
import math

class Turret_control(object):

    def __init__(self, max_locations, dist_per_pixel):
        """
        dist_per_pixel - in meters/pixel
        max_location - history of tracked locations
        """
        self._base_dist_per_pixel = dist_per_pixel
        self.max_locations = max_locations
        self._last_n_locations = queue.Queue(self.max_locations) # history of tracked locations along with their time stamps


    def _dist_per_pixel(self, depth):
        return self._base_dist_per_pixel/depth

    def get_azimuth_elevation(self, data, depth):
        """
        Takes in a pixel value and depth and returns the corresponding azimuth
        and elevation in radians
        @params:
            data - tuple (x, y, timestamp) - x, y are the pixel coordinates
            timestamp - in  miliseconds
            depth - depth in meters
        @return:
            theta_x, theta_y in degrees
            angular_v_x, angular_v_x in degrees/sec
        """
        # update the history data structure
        self._update_queue(data)

        # collect current data
        x, y, timestamp = data

        # retrieve previous timestep data
        previous_x, previous_y, previous_timestamp = list(self._last_n_locations.queue)[-1]

        # calculate deltas
        delta_x = x - previous_x
        delta_y = y - previous_y
        delta_t = (timestamp - previous_timestamp)/1000 # time diff in seconds

        # calculate arc lengths
        arclen_x = (delta_x)*(self._dist_per_pixel(depth))
        arclen_y = (delta_y)*(self._dist_per_pixel(depth))

        # calculate elevation and azimuth changes
        theta_x = math.degrees(arclen_x/depth)
        theta_y = math.degrees(arclen_y/depth)

        # calculate angular velocities
        v_x = delta_x/delta_t
        v_y = delta_y/delta_t
        angular_v_x = math.degrees(v_x/depth)
        angular_v_y = math.degrees(v_y/depth)
        return (theta_x, theta_y), (angular_v_x, angular_v_y)

    def _update_queue(self, data):
        """
        updates the the history queue
        """
        if self._list_n_locations.full():
            self._last_n_locations.get()
            self._list_n_locations.put(data)
        else:
            self._list_n_locations.put(data)




if __name__ == "__main__":
    pass
