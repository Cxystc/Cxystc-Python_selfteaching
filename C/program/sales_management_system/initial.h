#ifndef _INITIAL_H_//���û�ж���
#define _INITIAL_H_//��ִ������Ĵ���

typedef struct W {
    long long int Number ;
    long long int Product1 ; 
    long long int Product2 ; 
    long long int Product3 ; 
    long long int Product4 ; 
    long long int Product5 ; 
    int Amount1 ; 
    int Amount2 ;
    int Amount3 ;
    int Amount4 ;
    int Amount5 ;
    struct W *Next ;
} Workers ;//��������4������Ա��

//�����Ǵ����ѯ��Ӧ��Ʒ�����۶�Ľṹ�壻
typedef struct A{
    long long ProductNumber ; 
    int Amounta;
    int Amountb;
    int Amountc;
    int Amountd;//һ�����ĸ�Ա��
}Product_Statistics;

//�����Ǵ����ѯ��ӦԱ�������۶�Ľṹ��
typedef struct B{
    long long WorkerNumber; 
    int Amount1;
    int Amount2;
    int Amount3;
    int Amount4;
    int Amount5;//һ�������ֲ�Ʒ
}Worker_Statistics;
#endif
