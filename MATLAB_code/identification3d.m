% 'P' is a nx6 (or nx3) matrix containing identified objects in logFile.txt as following:

% successn xn yn errorn inliersn ration

% successn: bool meaning that n-th object meets the criteria of a vertical element
% [xn yn]: float coordinates of the n-th object
% errorn: square root of the squared distances of every point in the
% cluster of the n-th object to the model of the fitted line
% inliersn: inliers of the fitted line model in the cluster of the n-th
% object
% ration: inliersn divided by the total number of points in the n-th object
% cluster


prueba = 1;
num = 0; % set to 0 for last log
draw_veMap = 0;

if(num == 0)
    VE = load('logVE.txt');
    Odom = load('logOdom.txt');
    EKF = load('logEKF.txt');
    GPS = load('logGPS.txt');
    GPSRaw = load('logGPSRaw.txt');
else
    VE = load(strcat('test/ultima',num2str(prueba),'/',num2str(num),'logVE.txt'));
    Odom = load(strcat('test/ultima',num2str(prueba),'/',num2str(num),'logOdom.txt'));    
    EKF = load(strcat('test/ultima',num2str(prueba),'/',num2str(num),'logEKF.txt'));
    GPS = load(strcat('test/ultima',num2str(prueba),'/',num2str(num),'logGPS.txt'));
    GPSRaw = load(strcat('test/ultima',num2str(prueba),'/',num2str(num),'logGPSRaw.txt'));
end

if(prueba==1)
    theta_gps = -7.4; % test 1
elseif(prueba==2)
    theta_gps = -5.4; % test 2
end

veMap = load(strcat('map',num2str(prueba),'.csv'));

rotation = [cosd(theta_gps) sind(theta_gps); -sind(theta_gps) cosd(theta_gps)];

OdomCoord = [Odom(:,1) Odom(:,2)]; 
GPSCoord = [GPS(:,1) GPS(:,2)];
EKFCoord = [EKF(:,1) EKF(:,2)];
VECoord = [VE(:,2) VE(:,3)];

offsetGPS = GPSRaw(1,1:2)

OdomCoord = OdomCoord*rotation;
% GPSCoord = GPSCoord*rotation;
EKFCoord = EKFCoord*rotation;
VECoord = VECoord*rotation;
veMap = veMap*rotation;

OdomCoordGlob = OdomCoord + ones(size(OdomCoord,1),1)*offsetGPS;
EKFCoordGlob = EKFCoord + ones(size(EKFCoord,1),1)*offsetGPS;
PCoordGlob = VECoord + ones(size(VECoord,1),1)*offsetGPS;
veMapGlob = veMap + ones(size(veMap,1),1)*offsetGPS;
GPSCoordGlob = GPSRaw(:,1:2);

%Interpolate to get the errors
% OdomInt = 
radius = 0.5;
theta = linspace(0,2*pi);

if(size(VE,2) == 6)
    figure(1); title('error');
    hold on
    for i=1:size(VE,1)
        if(VE(i,1)==0)
            plot3(VECoord(i,1),VECoord(i,2),100*VE(i,4),'+r')
        else
            plot3(VECoord(i,1),VECoord(i,2),100*VE(i,4),'g+')
        end
    end
%     xlim([-30 150])
%     ylim([-20 50])
    grid
    
    if(draw_veMap)
        % Check identifications around ground truth values of object locations
        for i=1:length(veMap)
            x = radius*cos(theta) + veMap(i,1);
            y = radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'b-')

            x = 5*radius*cos(theta) + veMap(i,1);
            y = 5*radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'k-')

            plot3(veMap(i,1)*ones(2,1), veMap(i,2)*ones(2,1), [0 100], '-b')
        end
    end
    
    plot3(OdomCoord(:,1), OdomCoord(:,2), zeros(1,length(OdomCoord)), '-m')
    plot3(EKFCoord(:,1), EKFCoord(:,2), zeros(1,length(EKFCoord)), '-r')
    plot3(GPSCoord(:,1), GPSCoord(:,2), zeros(1,length(GPSCoord)), '-g')
    axis equal
    
    figure(2); title('inliers');
    hold on
    for i=1:size(VE,1)
        if(VE(i,1)==0)
            plot3(VECoord(i,1),VECoord(i,2),VE(i,5),'+r')
        else
            plot3(VECoord(i,1),VECoord(i,2),VE(i,5),'+g')
        end
    end
%     xlim([-30 150])
%     ylim([-20 50])
    grid
    
    if(draw_veMap)
        % Check identifications around ground truth values of object locations
        for i=1:length(veMap)
            x = radius*cos(theta) + veMap(i,1);
            y = radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'b-')

            x = 5*radius*cos(theta) + veMap(i,1);
            y = 5*radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'k-')

            plot3(veMap(i,1)*ones(2,1), veMap(i,2)*ones(2,1), [0 100], '-b')
        end
    end
    
    plot3(OdomCoord(:,1), OdomCoord(:,2), zeros(1,length(OdomCoord)), '-m')
    plot3(EKFCoord(:,1), EKFCoord(:,2), zeros(1,length(EKFCoord)), '-r')
    plot3(GPSCoord(:,1), GPSCoord(:,2), zeros(1,length(GPSCoord)), '-g')
    axis equal
    
    figure(3); title('ratio');
    hold on
    for i=1:size(VE,1)
        if(VE(i,1)==0)
            plot3(VECoord(i,1),VECoord(i,2),100*VE(i,6),'+r')
        else
            plot3(VECoord(i,1),VECoord(i,2),100*VE(i,6),'+g')
        end
    end
%     xlim([-30 150])
%     ylim([-20 50])
    grid
    
    if(draw_veMap)
        % Check identifications around ground truth values of object locations
        for i=1:length(veMap)
            x = radius*cos(theta) + veMap(i,1);
            y = radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'b-')

            x = 5*radius*cos(theta) + veMap(i,1);
            y = 5*radius*sin(theta) + veMap(i,2);
            plot3(x,y,zeros(1,length(theta)),'k-')

            plot3(veMap(i,1)*ones(2,1), veMap(i,2)*ones(2,1), [0 100], '-b')
        end
    end
    
    plot3(OdomCoord(:,1), OdomCoord(:,2), zeros(1,length(OdomCoord)), '-m')
    plot3(EKFCoord(:,1), EKFCoord(:,2), zeros(1,length(EKFCoord)), '-r')
    plot3(GPSCoord(:,1), GPSCoord(:,2), zeros(1,length(GPSCoord)), '-g')

    axis equal
    
    
elseif(size(VE,2) == 3)
    figure(1); title('identifications');
    hold on
    for i=1:size(VE,1)
        if(VE(i,1)==0)
            plot(VE(i,2),VE(i,3),'+r')
        else
            plot(VE(i,2),VE(i,3),'+g')
        end
    end
    xlim([-30 150])
    ylim([-20 50])
    grid
    
    % Check identifications around ground truth values of object locations
    
    for i=1:length(veMap)
        x = radius*cos(theta) + veMap(i,1);
        y = radius*sin(theta) + veMap(i,2);
        plot(x,y,'b')
        
        x = 5*radius*cos(theta) + veMap(i,1);
        y = 5*radius*sin(theta) + veMap(i,2);
        plot(x,y,'k')
    end
    
    plot(OdomCoord(:,1), OdomCoord(:,2), '-m')
    plot(EKFCoord(:,1), EKFCoord(:,2), '-r')
    plot(GPSCoord(:,1), GPSCoord(:,2), '-g')
    axis equal
    hold off
end

hold off






count = zeros(length(veMap),4);
% First column: positive identifications
% Second column: false negatives
% Third column: total number of identifications
% Fourth column: difference between positives and false negatives (better
% when closer to column 1)

for i=1:size(VE,1)
    for j=1:length(veMap)
        if((VECoord(i,1)-veMap(j,1))^2 + (VECoord(i,2)-veMap(j,2))^2 < radius^2)
            if (VE(i,1) == 1)
                count(j,1) = count(j,1) + 1;
            else
                count(j,2) = count(j,2) - 1;
            end
        end
        count(j,3) = count(j,1) - count(j,2);
        count(j,4) = count(j,1) + count(j,2);
    end
end

if(draw_veMap)
    count
end