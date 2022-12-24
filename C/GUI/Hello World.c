#include <windows.h>
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,LPSTR lpCmdLine,int nCmdShow)
{
    MessageBox (NULL,TEXT("Hello World"),TEXT("Welcome"),MB_OKCANCEL);
    return 0 ; 
}