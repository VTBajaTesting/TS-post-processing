clc; clear;

%Import Competition Data
%addpath('Z:\GPS Data','-end');
%MCDTest1.(data_name) = xlsread('MCDTest1.(data_name).csv', 'MCDTest1.(data_name)', 'K2111:N2611');
%save('MCDTest1.(data_name).mat','MCDTest1.(data_name)');

%load MCDTest1.(data_name);
fname = mfilename('fullpath');
[dirname, ~, ~] = fileparts(fname);
files_list = dir(dirname);
for f = 1:length(files_list)
    files_list(f)
    if endsWith(files_list(f).name, '.mat')
        MCDTest1 = load(files_list(f).name);
        data_name = fieldnames(MCDTest1);
        data_name = data_name{1};
        speed = MCDTest1.(data_name)(1:length(MCDTest1.(data_name)),4);
        latitude = MCDTest1.(data_name)(1:length(MCDTest1.(data_name)),1);
        longitude = MCDTest1.(data_name)(1:length(MCDTest1.(data_name)),2);
        altitude = MCDTest1.(data_name)(1:length(MCDTest1.(data_name)),3);

        i=1;
        accel = [0];
        while i < length(MCDTest1.(data_name))
            accel(i,1) = speed(i)-speed(i+1);
            i=i+1;
        end
        accel(length(MCDTest1.(data_name))) = accel(length(MCDTest1.(data_name))-1);
        %% Clean Data
        i=2;
        lon_75 = prctile(longitude,99.6);
        lon_25 = prctile(longitude,.05);
        lat_75 = prctile(latitude,99.6);
        lat_25 = prctile(latitude,.05);
        
        while i < length(MCDTest1.(data_name))
            %if longitude(i) > -77.1 || longitude(i) < -77.5
            %    longitude(i) = longitude(i-1);
            %end
            %if latitude(i) > 43.2 || latitude(i) < 43.068
            %    latitude(i) = latitude(i-1);
            %end
            if longitude(i) > lon_75 || longitude(i) < lon_25
                longitude(i) = longitude(i-1);
            end
            if latitude(i) > lat_75 || latitude(i) < lat_25
                latitude(i) = latitude(i-1);
            end
            if speed(i) > 50
                speed(i) = speed(i-1);
            end
            i=i+1;
        end
        % %% Plot Speed

        %% Plot Track
        % Create figure
        figure1 = figure('Name','Endurance Track Speed');

        % Create axes
        axes1 = axes('Parent',figure1);
        hold(axes1,'on');

        % Create scatter
        
        scatter(longitude,latitude,10,speed);

        % Create colorbar
        colorbar('peer',axes1);
        grid on;

        %% Speed Histogram
        maxspeed = max(speed);
        figure(3);
        speedmin = 5;
        selectspeed = [];
        for i = 1:length(speed)
            if speed(i) >= speedmin
                selectspeed(length(selectspeed)+1) = speed(i);
            end
        end
        histogram(selectspeed);
        xlim([5 30]);
        medianspeed = median(selectspeed);
    end
end