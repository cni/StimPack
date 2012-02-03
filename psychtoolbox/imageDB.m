function pth = imageDB;
% pth = imageDB
%
% returns the path for the image database on the local computer.
% Change this for different computers. This allows more flexibility
% in porting scripts from one place to another. First put in use
% 10/03, for rory's masking experiments (starting w/ expt 4).
%
% 10/03 ras.

pth = fullfile(fileparts(fileparts(which(mfilename))),'ImageDB');
%pth = fullfile('/home','cni','stimuli','ImageDB');

return

