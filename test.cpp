#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
using namespace std;


int main(void)
{
   
    int p1,p2,p3,b1,b2,b3,ptot,btot,i, deck_array[10];
    deck_array[0] = 8 * 16;
    for (i=1; i<=9;i++){
        deck_array[i] = 8 * 4;
    }

    __int64 combin, player_win, banker_win, tie_win;
    combin      = 1;
    player_win  = 0;
    banker_win  = 0;
    tie_win     = 0;
    
    for (p1=0; p1<=9; p1++)
    {
        combin*=deck_array[p1];
        deck_array[p1]--;
        for (p2=0; p2<=9; p2++)
        {
            combin*=deck_array[p2];
            deck_array[p2]--;
            for (p3=0; p3<=9; p3++)
            {
                combin*=deck_array[p3];
                deck_array[p3]--;
                for (b1=0; b1<=9; b1++)
                {  
                    combin*=deck_array[b1];
                    deck_array[b1]--;
                    for (b2=0; b2<=9; b2++)
                    {
                        combin*=deck_array[b2];
                        deck_array[b2]--;
                        for (b3=0; b3<=9; b3++)
                        {
                            combin*=deck_array[b3];
                            ptot=(p1+p2)%10;
                            btot=(b1+b2)%10;
                            if((ptot<8) && (btot<8))
                            {
                                if(ptot<=5){
                                    ptot=(p1+p2+p3)%10;
                                    
                                    if((btot<=2) || ((btot==3) && (p3!=8)) || ((btot == 4) && (p3 >=2) && (p3<=7)) || ((btot == 5) && (p3 >=4) && (p3<=7)) || ((btot == 6) && (p3 >=6) && (p3<=7))){
                                        btot=(b1+b2+b3)%10;
                                    }
                                }
                                else{
                                    if (btot<=5){
                                       btot=(b1+b2+b3)%10; 
                                    }
                                }
                            }
                            if (ptot>btot){
                                player_win  += combin;
                            }
                            else if (ptot<btot){
                                banker_win  += combin;
                            }
                            else{
                                tie_win  += combin;
                            }
                            combin /= deck_array[b3];
                        }
                        deck_array[b2]++;
                        combin /= deck_array[b2];
                    }
                    deck_array[b1]++;
                    combin /= deck_array[b1];
                }
                deck_array[p3]++;
                combin /= deck_array[p3];
            }
            deck_array[p2]++;
            combin /= deck_array[p2];
        }
        deck_array[p1]++;
        combin /= deck_array[b2];
    }

    printf("Player wins=\t%I64i\n", player_win);
    printf("Banker wins=\t%I64i\n", banker_win);
    printf("Tie wins=\t%I64i\n", tie_win);
    __int64 tot_combin = player_win + banker_win + tie_win;
    double player_prob = (double)player_win / (double)tot_combin;
    double banker_prob = (double)banker_win / (double)tot_combin;
    double tie_prob    = (double)tie_win / (double)tot_combin;
    printf("Player wins=\t%f\n", player_prob);
    printf("Banker wins=\t%f\n", banker_prob);
    printf("Tie wins=\t%f\n", tie_prob);
    double player_ev = player_prob - banker_prob;
    double banker_ev = 0.95 * banker_prob - player_prob;
    double tie_ev = 8 * tie_prob - player_prob - banker_prob;
    printf("Player EV=\t%I64i\n", player_ev);
    printf("Banker EV=\t%I64i\n", banker_ev);
    printf("Tie EV=\t%I64i\n", tie_ev);
    
    // return 0;
}

