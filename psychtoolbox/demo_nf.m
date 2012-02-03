#!/usr/bin/env octave

%function GarboriumDemo(ngabors)
%
% You can exit the demo by pressing any key on the keyboard.
%
% This demo needs recent graphics hardware with floating point framebuffer
% support: ATI Radeon X1000 and later, NVidia GeForce 6000 and later.

% try face, place, scene, house, animal, vehicle, car, bird, fish, instrument, texture (see categoryDirs.m)
imageTypes = {'house','sculpt'};

% PTB-3 correctly installed and functional? Abort otherwise.
AssertOpenGL;

% Set number of gabor patches to 200 if no number provided:
if nargin < 1 || isempty(ngabors)
    ngabors = 100;
end

fprintf('Will draw %i image patches per frame.\n', ngabors);

Screen('Preference', 'SkipSyncTests', 1 );

% Select screen with maximum id for output window:
screenid = max(Screen('Screens'));

bgColor = 128;
speed = 2;

% Open a fullscreen, onscreen window with gray background. Enable 32bpc
% floating point framebuffer via imaging pipeline on it, if this is possible
% on your hardware while alpha-blending is enabled. Otherwise use a 16bpc
% precision framebuffer together with alpha-blending. We need alpha-blending
% here to implement the nice superposition of overlapping gabors. The demo will
% abort if your graphics hardware is not capable of any of this.
PsychImaging('PrepareConfiguration');
PsychImaging('AddTask', 'General', 'FloatingPoint32BitIfPossible');
% rect is left,top,right,bottom
[win winRect] = PsychImaging('OpenWindow', screenid, bgColor, [1920,0,3200,800]);

% Retrieve size of window in pixels, need it later to make sure that our
% moving gabors don't move out of the visible screen area:
[w, h] = RectSize(winRect);

% Query frame duration: We use it later on to time 'Flips' properly for an
% animation with constant framerate:
ifi = Screen('GetFlipInterval', win);

% Enable alpha-blending, set it to a blend equation useable for linear
% superposition with alpha-weighted source. This allows to linearly
% superimpose gabor patches in the mathematically correct manner, should
% they overlap. Alpha-weighted source means: The 'globalAlpha' parameter in
% the 'DrawTextures' can be used to modulate the intensity of each pixel of
% the drawn patch before it is superimposed to the framebuffer image, ie.,
% it allows to specify a global per-patch contrast value:
Screen('BlendFunction', win, GL_SRC_ALPHA, GL_ONE);

maxContrast = 0.5;
%im = loadCategoryImages(1, imageTypes{1});
sz = [120 120];
x = sz(1)/2; y = sz(2)/2;
[gab_x gab_y] = meshgrid(0:(sz(1)-1), 0:(sz(2)-1));
x_factor=-1*(gab_x-x).^2;
y_factor=-1*(gab_y-y).^2;
varScale = sz(1)*8;
g = maxContrast * exp(x_factor/varScale+y_factor/varScale);
for(jj=1:numel(imageTypes))
    im = loadCategoryImages(ngabors, imageTypes{jj});
    for(ii=1:numel(im))
        if(~all(size(im{ii})==sz))
            [XI, YI] = meshgrid(linspace(1, size(im{ii},2), sz(2)), linspace(1, size(im{ii},2), sz(2)));
            %curIm = interp2(double(im{ii}), XI(:), YI(:), "linear", 127.5);
            curIm = imremap(double(im{ii}), XI, YI, "linear", 127.5);
        else
            curIm = double(im{ii});
        end
        m = (curIm./127.5 - 1.0) .* g;
        imtex{jj}(ii) = Screen('MakeTexture', win, m, [], [], 2);
    end
    clear im;
end
numBlocks = numel(imtex);

% Build drawable texture from gabor matrix: We set the 'floatprecision' flag to 2,
% so it is internally stored with 32 bits of floating point precision and
% sign. This allows for effectively 8 million (23 bits) of contrast levels
% for both the positive- and the negative "half-lobe" of the patch -- More
% than enough precision for any conceivable display system:

% Preallocate array with destination rectangles:
% This also defines initial gabor patch orientations, scales and location
% for the very first drawn stimulus frame:
texrect = Screen('Rect', imtex{1}(1));
inrect = repmat(texrect', 1, ngabors);

dstRects = zeros(4, ngabors);
for i=1:ngabors
    scale(i) = 2*(0.5 + 0.5 * randn);
    dstRects(:, i) = CenterRectOnPoint(texrect * scale(i), rand * w, rand * h)';
end

sflags = 0;
srcRect = [];

% Preallocate array with rotation angles:
rotAngles = rand(1, ngabors) * 45;
driftAngles = rand(1, ngabors) * 360;

count = 0;
curBlockNum = 1;

% Wait for a keypress
startKey = KbName('space'); 
endKey = KbName('escape');
Screen('DrawText',win,'Waiting to start...');
vbl = Screen('Flip', win);
[a,b,keyCode] = KbCheck();
while(~keyCode(startKey))
    sleep(0.1);
    [a,b,keyCode] = KbCheck();
end
Screen('DrawText',win,'Sending scan trigger...');
vbl = Screen('Flip', win);
sleep(0.5);

% Initially sync us to VBL at start of animation loop.
vbl = Screen('Flip', win);
tstart = vbl;
startSecs = time();
%unix('/usr/local/bin/startScan');

% Animation loop: Run until any keypress:
[a,b,keyCode] = KbCheck();
while(~keyCode(endKey))
    % Step one: Batch-Draw all gabor patches at the positions and
    % orientations computed during last loop iteration: Here we fix
    % 'globalAlpha' - and therefore contrast - to 0.5, ie., 50% of
    % displayable range. Actually its less than 0.5, depending on the
    % inherent contrast of the gabor defined above in matrix 'm'.
    Screen('DrawTextures', win, imtex{curBlockNum}, srcRect, dstRects, rotAngles, [], 0.5, [], [], sflags);

    elapsed = time() - startSecs;
    if(elapsed>12)
        curBlockNum = curBlockNum+1;
        if(curBlockNum>numBlocks)
             curBlockNum = 1;
        end
        startSecs = time();
    end

    % Fixation point:
    Screen('FillOval', win, [255,0,0], [w/2-5,h/2-5,w/2+5,h/2+5]);

    % Mark drawing ops as finished, so the GPU can do its drawing job while
    % we can compute updated parameters for next animation frame. This
    % command is not strictly needed, but it may give a slight additional
    % speedup, because the CPU can compute new stimulus parameters in
    % Matlab, while the GPU is drawing the stimuli for this frame.
    % Sometimes it helps more, sometimes less, or not at all, depending on
    % your system and code, but it only seldomly hurts.
    % performance...
    Screen('DrawingFinished', win);
    
    % Compute updated positions and orientations for next frame. This code
    % is vectorized, but could be probably optimized even more. Indeed,
    % these few lines of Matlab code are the main speed-bottleneck for this
    % demos animation loop on modern graphics hardware, not the actual drawing
    % of the stimulus. The demo as written here is CPU bound - limited in
    % speed by the speed of your main processor.

    % Compute new orientation for each patch in next frame:
    rotAngles = rotAngles + randn(1, ngabors);
    driftAngles = driftAngles + 10*randn(1, ngabors);
    
    % Compute centers of all patches, then shift them in new direction of
    % motion 'rotAngles', use the mod() operator to make sure they don't
    % leave the window display area. Its important to use RectCenterd and
    % CenterRectOnPointd instead of RectCenter and CenterRectOnPoint,
    % because the latter ones would round all results to integral pixel
    % locations, which would make for an odd and jerky movement. It is
    % also important to feed all matrices and vectors in proper format, as
    % these routines are internally vectorized for higher speed.
    [x y] = RectCenterd(dstRects);
    x = mod(x + cos(driftAngles/360*2*pi)*speed, w);
    y = mod(y + sin(driftAngles/360*2*pi)*speed, h);

    % Recompute dstRects destination rectangles for each patch, given the
    % 'per gabor' scale and new center location (x,y):
    dstRects = CenterRectOnPointd(inrect .* repmat(scale,4,1), x, y);
    
    % Done. Flip one video refresh after the last 'Flip', ie. try to
    % update the display every video refresh cycle if you can.
    % This is the same as Screen('Flip', win);
    % but the provided explicit 'when' deadline allows PTB's internal
    % frame-skip detector to work more accurately and give a more
    % meaningful report of missed deadlines at the end of the script. Not
    % important for this demo, but here just in case you didn't know ;-)
    vbl = Screen('Flip', win, vbl + 0.5 * ifi);

 % Next loop iteration...
    count = count + 1;
    [a,b,keyCode] = KbCheck();
end

% Done. Last flip to take end timestamp and for stimulus offset:
vbl = Screen('Flip', win);

% Print the stats:
count
avgfps = count / (vbl - tstart)

% Close onscreen window, release all ressources:
Screen('CloseAll');

% Done.
%return;
