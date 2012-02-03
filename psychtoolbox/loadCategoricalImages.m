function images = loadCategoricalImages(num,varargin);
% images = loadCategoryImages(numImages,categories);
%
% load, from the imageDB, a specified # of images from the selected
% categories.
%
% The categories can be any category specified in categoryDirs.m.
%
% The code will load a total of num files, broken down evenly
% among the selected categories.
%
% ras, 10/04
images = {};

if nargin < 2
    help loadCategoryImages;
    return
end

% will want to add code here to parse
% flags, like 'shuffle' to shuffle images

categories = varargin;
nCats = length(categories);
imgsPerCat = ceil(num/nCats);

for c = 1:nCats
    % get the list of image names for this category
    imlist = categoryImages(categories{c},'fullpath');

    imlist = shuffle(imlist);

    % load the images
    for i = 1:imgsPerCat
        images = [images {imread(imlist{i},'jpg')}];
    end
end

% cut any extra, roundoff-error images
images = images(1:num);
return;


function dirList = categoryDirs(catName);
% This function returns a cell-of-strings containing directory names
% where images belonging to a desired category can be found. It removes the
% clutter of having all the possibilties spelled out/commented out at the beginning.
%
% if an invalid category is specified, it errors.
%
% 10/03 ras.
if ~exist('imageDB','file')
	fprintf('Check your paths -- you need the file imageDB.m. \n');
	return
end

% remove trailing s's -- a crude way to be compatible with plural/singular category specification
if isequal(catName(end),'s')
	catName = catName(1:end-1);
end

switch lower(catName)
case 'animal',
	dirList= { ...
	fullfile(imageDB,'jpgcats') ...
	fullfile(imageDB,'jpgdogs') ...
	fullfile(imageDB,'jpghorse') ...
	fullfile(imageDB,'jpgdonkey') ...
	fullfile(imageDB,'jpgbirds') ...
	fullfile(imageDB,'jpgfish') ...
	};
case {'4leggedanimal','animalnew','newanimal'},
	dirList= { ...
	fullfile(imageDB,'jpgnew4leggedanimals') ...
	};
case {'animalnoface','animalsmallface'},
	dirList= { ...
	fullfile(imageDB,'animalnoface') ...
	};

case {'airplane','plane'},
	dirList = { ...
	fullfile(imageDB,'jpgairplanes','fighterjpg') ...
	fullfile(imageDB,'jpgairplanes','planejpg') ...
	fullfile(imageDB,'jpgairplanes','jetjpg') ...
	};
case 'vehicle',
	dirList= [categoryDirs('airplane'); categoryDirs('boat'); categoryDirs('car')];
case 'bird',
	dirList= { ...
	fullfile(imageDB,'jpg_animals','jpgbirds','assortedbirds') ...
	fullfile(imageDB,'jpg_animals','jpgbirds','ducks') ...
	fullfile(imageDB,'jpg_animals','jpgbirds','parrots') ...
	fullfile(imageDB,'jpg_animals','jpgbirds','pigeons') ...
	};
case 'boat',
	dirList = { ...
	fullfile(imageDB,'jpgboats','assortedboats') ...
	fullfile(imageDB,'jpgboats','motorboats') ...
	fullfile(imageDB,'jpgboats','sailboats') ...
	};
case 'cat',
	dirList = { ...
	fullfile(imageDB,'jpgcats','jpghousecat') ...
	fullfile(imageDB,'jpgcats','jpgassortedcat') ...
	};
case 'car',
	dirList = { ...
	fullfile(imageDB,'jpgcar_noBG') ...
	};
case 'dog',
	dirList= { ...
	fullfile(imageDB,'jpgdogs') ...
	};
case 'face',
	dirList= { ...
	fullfile(imageDB,'jpgfaces','man') ...
	fullfile(imageDB,'jpgfaces','woman') ...
	fullfile(imageDB,'jpgfaces','child') ...
	};
case {'man','male','men'}
	dirList= { ...
	fullfile(imageDB,'jpgfaces','man') ...
	};
case {'female','woman','women'}
	dirList= { ...
	fullfile(imageDB,'jpgfaces','woman') ...
	};
case {'child'}
	dirList= { ...
	fullfile(imageDB,'jpgfaces','child') ...
	};
case 'donkey',
	dirList= { ...
	fullfile(imageDB,'jpgdonkey') ...
	};
case {'famous'}
	dirList= { ...
	fullfile(imageDB,'jpgfaces','brad') ...
	fullfile(imageDB,'jpgfaces','cindy') ...
	fullfile(imageDB,'jpgfaces','claudia') ...
	fullfile(imageDB,'jpgfaces','harrisonford') ...
	fullfile(imageDB,'jpgfaces','julia') ...
	};
case 'feline',
	dirList= { ...
	fullfile(imageDB,'jpgcats','jpghousecat') ...
	fullfile(imageDB,'jpgcats','jpgassortedcat') ...
	fullfile(imageDB,'jpgcats','jpglion') ...
	};
case 'fish',
	dirList= { ...
	fullfile(imageDB,'jpg_animals','jpgfish','assortedfish') ...
	fullfile(imageDB,'jpg_animals','jpgfish','jpgshark') ...
	};
case {'boat+car','boats+car','car+boat','cars+boat'},
	dirList = [categoryDirs('boat') categoryDirs('car')];
case 'horse',
	dirList= { ...
	fullfile(imageDB,'jpghorse') ...
	};
case 'anim+vehicle',
	dirList= [categoryDirs('bird+fish') categoryDirs('vehicle')];
case {'bird+fish','birds+fish'},
	dirList= [categoryDirs('bird') categoryDirs('fish')];
case 'instrument',
	dirList = { ...
	fullfile(imageDB,'jpg_musical','jpgbrass') ...
	fullfile(imageDB,'jpg_musical','jpgsaxophone') ...
	fullfile(imageDB,'jpg_musical','jpgtrumpet') ...
	fullfile(imageDB,'jpg_musical','jpgguitars') ...
	fullfile(imageDB,'jpg_musical','strings') ...
	fullfile(imageDB,'jpg_musical','jpgpianos','assorted_jpg') ...
	fullfile(imageDB,'jpg_musical','jpgpianos','grand_jpg') ...
	fullfile(imageDB,'jpg_musical','jpgpianos','upright_jpg') ...
	};
case 'scene',
	dirList = { ...
	fullfile(imageDB,'bwscenes') ...
	};
case 'house',
	dirList = { ...
	fullfile(imageDB,'jpghouses','all') ...
	};
case 'place',
	dirList = { ...
	fullfile(imageDB,'bwscenes') ...
	fullfile(imageDB,'jpghouses','all') ...
	};
case {'line','Dave'},
	dirList = { ...
	fullfile(imageDB,'jpgline','uni_stim_15') ...
	fullfile(imageDB,'jpgline','uni_stim_105') ...
	fullfile(imageDB,'jpgline','vehicle','car') ...
	fullfile(imageDB,'jpgline','animal','mammal') ...
	fullfile(imageDB,'jpgline','linefaces') ...
	fullfile(imageDB,'jpgline','animal','dinosaur') ...
	};
case {'lineface'},
	dirList = { ...
	fullfile(imageDB,'jpgline','linefaces') ...
	};
case {'linecar'},
	dirList = { ...
	fullfile(imageDB,'jpgline','vehicle','car') ...
	};
case {'linevehicle'},
	dirList = { ...
	fullfile(imageDB,'jpgline','vehicle','car') ...
	fullfile(imageDB,'jpgline','vehicle') ...
	};
case {'lineanimal'},
	dirList = { ...
	fullfile(imageDB,'jpgline','animal','mammal') ...
	fullfile(imageDB,'jpgline','animal','dinosaur') ...
	};
case {'linedino','linedinosaur'},
	dirList = { ...
	fullfile(imageDB,'jpgline','animal','dinosaur') ...
	};
case {'linemammal'},
	dirList = { ...
	fullfile(imageDB,'jpgline','animal','mammal') ...
	};
case {'linescrambled'},
	dirList = { ...
	fullfile(imageDB,'jpgline','scrambled') ...
	};
case {'linesubset','linesubset32','subset32'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','face') ...
	fullfile(imageDB,'jpgline','subset32','vehicle') ...
	fullfile(imageDB,'jpgline','subset32','animal') ...
	};
case {'subset32face'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','face') ...
	};
case {'subset32vehicle'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','vehicle') ...
	};
case {'subset32animal'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','animal') ...
	};
case {'subset32abstract'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','abstract') ...
	};
case {'subset32scrambled'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset32','scrambled') ...
	};
case {'subset12face'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset12','face') ...
	};
case {'subset12vehicle','subset12car'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset12','car') ...
	};
case {'subset12rotated'}, % rotated versions of subset 12 objects
	dirList = { ...
	fullfile(imageDB,'jpgline','subset12','rotated') ...
	};
case {'subset12animal'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset12','animal') ...
	};
case {'subset12scrambled'},
	dirList = { ...
	fullfile(imageDB,'jpgline','subset12','scrambled') ...
	};
case {'sculpt','sculpture','abstract','novel'}
	dirList = { ...
	fullfile(imageDB,'jpgsculpt_noBG') ...
	};
% 	fullfile(imageDB,'jpgsculpt_rastemp') ...
case {'coarsescrambled','scrambledcoarse'}
	dirList = { ...
    fullfile(imageDB,'roryscrambledcoarse') ...
	};
case {'texture','scrambled'}
	dirList = { ...
    fullfile(imageDB,'roryscrambledfine') ...
	};
% 	fullfile(imageDB,'SCRAMBLED_JPG') ...
% 	fullfile(imageDB,'jpgtextures') ...
otherwise,
	error('Invalid category specified.');
	return
end

% check that all the specified dirs exist
i = 1;
while i <= length(dirList)
	if ~exist(dirList{i},'dir')
		fprintf('categoryDirs: dir %s not found, removing from list.\n',dirList{i});
		dirList = {dirList{1:i-1} dirList{i+1:end}};
	end
	i = i + 1;
end

% looks nicer as a column vector
dirList = dirList(:);
return;



function imgList = categoryImages(varargin);
% imgList = categoryImages(categories,[options]);
%
% returns a list of image files for the specified category/categories.
%
% categories can be a string containing one category name, or
% a cell-of-strings containing several category names. For a list of
% acceptable category names, see categoryDirs.
%
% imgList is a cell-of-strings, containing paths relative to the imageDB,
% unless the 'fullpath' option is set,  in which case the full path of each
% image will be returned.
%
% If several categories of image are specified, the images will be concatenated
% in the output list.  Images will also be shuffled, unless the 'noshuffle' option is
%specified.
%
% Dependencies: categoryDirs, imageDB.
%
% first written for masking expt 4: stim strength/priming.
%
% 10/03 ras.
% 02/16/04 ras -- now recursively adds subdirectories.
if nargin < 1
	help categoryImages
    return
end

%%%%% parameters
stripPathFlag = 1;
shuffleFlag = 0;
recursionFlag = 1;

% be ready to accept nested cells in inputs
varargin = unNestCell(varargin);
cat = varargin;

%%%%% parse the options
for i = 1:length(varargin)
	if ischar(varargin{i})
        switch lower(varargin{i})
		case 'fullpath',
			stripPathFlag = 0;
			cat = {varargin{1:i-1} varargin{i+1:end}};
		case 'noshuffle',
			shuffleFlag = 0;
			cat = {varargin{1:i-1} varargin{i+1:end}};
		case 'shuffle',
			shuffleFlag = 1;
			cat = {varargin{1:i-1} varargin{i+1:end}};
		case 'norecursion',
			recursionFlag = 0;
			cat = {varargin{1:i-1} varargin{i+1:end}};
		otherwise,
			% ignore
		end
    end
end

dirList = {};
for i = 1:length(cat)
    dirList = [dirList categoryDirs(cat{i})'];
end

if recursionFlag==1 % find subdirectories and look in them
    cnt = 1;
    while (cnt <= length(dirList)) & (cnt<50)
        w = dir(dirList{cnt});
        for j = 1:length(w)
            if w(j).isdir && ~ismember(w(j).name,{'.' '..'})
                dirList{end+1} = fullfile(dirList{cnt},w(j).name);
            end
        end
        cnt = cnt + 1;
    end
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% generate list of image files
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
imgList = {};
cnt = 1;
for i = 1:length(dirList)
    nextdir = dirList{i};
    fprintf('%s ...\n',nextdir);
    w = dir(fullfile(nextdir,'*.jpg'));
    numfiles = length(w);
    for j = 1:numfiles
        imgList{cnt} = fullfile(dirList{i},w(j).name);
        cnt = cnt + 1;
    end
end

if stripPathFlag
    % paths will be specified relative to the imageDB path:
    % remove the beginning of each path, which specifies imageDB location
    n = length(imageDB) + 1;
    for i = 1:length(imgList)
        imgList{i} = imgList{i}(n:end);
    end
end

if shuffleFlag
    % shuffle image order
    imgList = shuffle(imgList);
end

% looks nicer as a column vector
imgList = imgList(:);

return;



function cellOut = unNestCell(cellIn);
% cellOut = unNestCell(cellIn):
%
% takes a cell which may have sub-cells as entries, and 'flattens out' the
% subentries. The output cell has no sub-cells: instead, wherever the cell
% entry would be, several entries are added containing the contents of that
% cell. Works recursively. Only works on cell arrays right now (not
% matrices of cells).
%
% 11/07/03 ras.
if nargin==0 | ~iscell(cellIn);
    help unNestCell;
    return;
end

cellOut = {};

for i = 1:length(cellIn)
    if iscell(cellIn{i})
        expand = unNestCell(cellIn{i});
        cellOut = {cellOut{1:end} expand{1:end}};
    else
        cellOut = {cellOut{1:end} cellIn{i}};
    end
end

return;

