#include <iostream>
#include <vector>

using namespace std;

class solution {
public:
    bool Find(int target, vector<vector<int>> array) {
        bool found = false;
        int rows = array.size();
        int columns = array[0].size();
        if(rows>0&&columns>0)
        {
            int row = 0;
            int column = columns-1;
            while(row<rows && column>=0)
            {;
                if(array[row][column]==target)
                {
                    found = true;
                    break;
                }
                else if(array[row][column]>target)
                {
                    --column;
                }
                else
                    ++row;
            }
        }
        return found;
    }

};
int main() {
    solution s;
    vector<vector<int>> array = {{1,2,8,9},{2,4,9,12},{4,7,10,13},{6,8,11,15}};
    int target = 7;
    cout<<s.Find(target,array);
    return 0;
}