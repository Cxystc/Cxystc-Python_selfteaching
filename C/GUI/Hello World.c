#include <windows.h>
#include <stdio.h>
LRESULT CALLBACK WindowProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);             //�ص���������
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) // Win32�������
{
    char szTitile[] = "���۹���ϵͳ";
    char szClassName[] = "ֽ���ϴ�ϵͳ";
    //��ƴ�����
    WNDCLASS wd1; //�������ʵ����

    //��д��������Ӧ����Ϣ(��Ҫ)
    wd1.cbClsExtra = 0;                                       //��Ķ��⸽���ֽ���
    wd1.cbWndExtra = 0;                                       //���ڶ���ĸ����ֽ���
    wd1.hbrBackground = (HBRUSH)GetStockObject(DKGRAY_BRUSH); //������ɫ
    wd1.hCursor = LoadCursor(NULL, IDC_ARROW);                //�����ʽ
    wd1.hIcon = LoadIcon(NULL, IDI_WINLOGO);                  //ͼ����ʽ
    wd1.hInstance = hInstance;                                //ʵ�����
    wd1.lpfnWndProc = WindowProc;                             //�ص�����,��ϵͳ����
    wd1.lpszClassName = szClassName;                          //����������
    wd1.lpszMenuName = NULL;                                  //�˵�����
    wd1.style = CS_HREDRAW | CS_VREDRAW;                      //��������,������ˮƽ�ػ�����ֱ�ػ�


    //ע�ᴰ����
    RegisterClass(&wd1);

    //��������
    HWND hWnd ;
    hWnd = CreateWindow(
        szClassName, 
        szTitile,
        WS_OVERLAPPEDWINDOW | WS_CLIPSIBLINGS,
        0,0,//λ��
        600,400,//��С
        NULL,//������
        NULL,//�˵�
        hInstance,//ʵ�����
        NULL//���ڴ�������
    );//����һ����������
    
    ShowWindow(hWnd, SW_SHOWNORMAL);
    UpdateWindow(hWnd);//ˢ��

    
}
