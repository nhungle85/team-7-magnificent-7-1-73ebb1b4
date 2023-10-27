*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move to position 5,5                5             4             0                     NORTH         5           5           1
Move to position 5,5              5             4             0                     NORTH         5           5           1
Move to position 5,6                5             7             100                   SOUTH         5           6           101
Move to position 2,2                1             2             50                    EAST          2           2           51
Bounceback to north 0,9             0             9             56                    NORTH         0           9           57
Move to position 4,6                5             6             1                     WEST          4           6           2
Bounceback to west 0,0              0             0             73                    WEST          0           0           74
Move to position 9,1                9             0             1023                  NORTH         9           1           1024
Bounceback to East 9,9              9             9             3                     EAST          9           9           4
Move to position 0,1                0             0             103                   NORTH         0           1           104

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}