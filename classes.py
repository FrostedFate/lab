class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        This method is used to initialize the TV object.
        :param TV_Channel: This is the initial TV channel.
        :param TV_Volume: This is the initial TV volume.
        :param TV_ISON: This is the initial TV status.
        """
        self.__TV_Channel = Television.MIN_CHANNEL
        self.__TV_VOLUME = Television.MIN_VOLUME
        self.__TV_ISON = False

        pass

    def power(self):
        """
        This turns the tv on and off
        :param TV_ISON: This is the TV status.
        """

        

        if self.__TV_ISON == False:
            self.__TV_ISON = True
        else:
            self.__TV_ISON = False
        pass

    def channel_up(self):
        """
        This method should be used to adjust the TV channel by incrementing its value up.
        :param TV_Channel: This is the TV channel.
        :param TV_ISON: This is the TV status.
        :param MAX_CHANNEL: This is the maximum TV channel.
        :param MIN_CHANNEL: This is the minimum TV channel.
        """

        if self.__TV_ISON == True:
            self.__TV_Channel = self.__TV_Channel + 1
            if self.__TV_Channel > Television.MAX_CHANNEL:
                self.__TV_Channel = Television.MIN_CHANNEL

        pass

    def channel_down(self):
        """
        This method should be used to adjust the TV channel by decrementing its value down.
        :param TV_Channel: This is the TV channel.
        :param TV_ISON: This is the TV status.
        :param MAX_CHANNEL: This is the maximum TV channel.
        :param MIN_CHANNEL: This is the minimum TV channel.
        """

        if self.__TV_ISON == True:
            self.__TV_Channel = self.__TV_Channel - 1
            if self.__TV_Channel < Television.MIN_CHANNEL:
                self.__TV_Channel = Television.MAX_CHANNEL


        pass

    def volume_up(self):
        """
        This method should be used to adjust the TV volume by incrementing its value up.
        :param TV_Volume: This is the TV volume.
        :param TV_ISON: This is the TV status.
        :param MAX_VOLUME: This is the maximum TV volume.
        :param MIN_VOLUME: This is the minimum TV volume.
        """

        if self.__TV_ISON == True:
            self.__TV_VOLUME = self.__TV_VOLUME + 1
            if self.__TV_VOLUME > Television.MAX_VOLUME:
                self.__TV_VOLUME = Television.MAX_VOLUME

        pass

    def volume_down(self):
        """
        This method should be used to adjust the TV volume by decrementing its value down.
        :param TV_Volume: This is the TV volume.
        :param TV_ISON: This is the TV status.
        :param MAX_VOLUME: This is the maximum TV volume.
        :param MIN_VOLUME: This is the minimum TV volume.
        """

        if self.__TV_ISON == True:
            self.__TV_VOLUME = self.__TV_VOLUME - 1
            if self.__TV_VOLUME < Television.MIN_VOLUME:
                self.__TV_VOLUME = Television.MIN_VOLUME

        pass

    def __str__(self):
        """
        - This method should be used to return the TV status using this format: "TV is on channel X at volume Y"
        """
        Reader = "TV status: Is on = " + str(self.__TV_ISON) + ", Channel = " + str(self.__TV_Channel) + ", Volume = " + str(self.__TV_VOLUME)
        return Reader
       