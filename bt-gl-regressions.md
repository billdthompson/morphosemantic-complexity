```
Show in New WindowClear OutputExpand/Collapse Output
Column `langCode`/`ISO_639` joining factors with different levels, coercing to character vectorColumn `langCode` joining character vector and factor, coercing into character vector
Show in New WindowClear OutputExpand/Collapse Output
Joining, by = "langCode"
Show in New WindowClear OutputExpand/Collapse Output
Joining, by = "langCode"
Show in New WindowClear OutputExpand/Collapse Output
corrplot 0.84 loaded
Show in New WindowClear OutputExpand/Collapse Output

Call:
lm(formula = C_WALS ~ semanticDistanceAll + morpho_sum + zeroprop_raw, 
    data = .)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.18764 -0.04606  0.01243  0.05921  0.18154 

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)   
(Intercept)          0.424823   0.140600   3.021  0.00533 **
semanticDistanceAll  0.007728   0.002675   2.889  0.00737 **
morpho_sum           0.002538   0.001099   2.310  0.02848 * 
zeroprop_raw        -0.300385   0.148582  -2.022  0.05286 . 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.09025 on 28 degrees of freedom
  (5 observations deleted due to missingness)
Multiple R-squared:  0.6672,	Adjusted R-squared:  0.6315 
F-statistic: 18.71 on 3 and 28 DF,  p-value: 7.359e-07

Modify Chunk OptionsRun All Chunks AboveRun Current Chunk
Show in New WindowClear OutputExpand/Collapse Output

Call:
lm(formula = C_WALS ~ semanticDistanceAll + morpho_sum + zeroprop_raw, 
    data = .)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.18764 -0.04606  0.01243  0.05921  0.18154 

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)   
(Intercept)          0.424823   0.140600   3.021  0.00533 **
semanticDistanceAll  0.007728   0.002675   2.889  0.00737 **
morpho_sum           0.002538   0.001099   2.310  0.02848 * 
zeroprop_raw        -0.300385   0.148582  -2.022  0.05286 . 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.09025 on 28 degrees of freedom
  (5 observations deleted due to missingness)
Multiple R-squared:  0.6672,	Adjusted R-squared:  0.6315 
F-statistic: 18.71 on 3 and 28 DF,  p-value: 7.359e-07


Call:
lm(formula = C_WALS ~ semanticDifferenceVarAll + morpho_sum + 
    zeroprop_raw, data = .)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.18118 -0.06250  0.01043  0.06468  0.19028 

Coefficients:
                          Estimate Std. Error t value Pr(>|t|)   
(Intercept)               0.431280   0.140766   3.064  0.00479 **
semanticDifferenceVarAll  0.010876   0.003844   2.830  0.00852 **
morpho_sum                0.001945   0.001094   1.778  0.08629 . 
zeroprop_raw             -0.303036   0.149665  -2.025  0.05252 . 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.09067 on 28 degrees of freedom
  (5 observations deleted due to missingness)
Multiple R-squared:  0.664,	Adjusted R-squared:  0.628 
F-statistic: 18.45 on 3 and 28 DF,  p-value: 8.379e-07
```

Note that `C_WALS` was not available for Norwegian (nno and nnb), Galician, Slovak, and Chinese Mandarin


We can repeat this analysis with `D~structure` as the dependent variable:

```

Call:
lm(formula = D_structure ~ semanticDistanceAll + morpho_sum + 
    zeroprop_raw, data = .)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.08720 -0.03741 -0.01508  0.03383  0.17978 

Coefficients:
                     Estimate Std. Error t value Pr(>|t|)    
(Intercept)          0.191258   0.089469   2.138  0.04028 *  
semanticDistanceAll  0.008970   0.001755   5.111 1.44e-05 ***
morpho_sum           0.002472   0.000715   3.458  0.00156 ** 
zeroprop_raw        -0.118695   0.093979  -1.263  0.21571    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.06158 on 32 degrees of freedom
  (1 observation deleted due to missingness)
Multiple R-squared:  0.7718,	Adjusted R-squared:  0.7504 
F-statistic: 36.08 on 3 and 32 DF,  p-value: 2.211e-10


Call:
lm(formula = D_structure ~ semanticDifferenceVarAll + morpho_sum + 
    zeroprop_raw, data = .)

Residuals:
      Min        1Q    Median        3Q       Max 
-0.093610 -0.038199 -0.006357  0.043096  0.183378 

Coefficients:
                           Estimate Std. Error t value Pr(>|t|)    
(Intercept)               0.1910750  0.0889690   2.148   0.0394 *  
semanticDifferenceVarAll  0.0129110  0.0025042   5.156 1.26e-05 ***
morpho_sum                0.0017703  0.0007127   2.484   0.0184 *  
zeroprop_raw             -0.1128805  0.0941361  -1.199   0.2393    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.06133 on 32 degrees of freedom
  (1 observation deleted due to missingness)
Multiple R-squared:  0.7736,	Adjusted R-squared:  0.7524 
F-statistic: 36.45 on 3 and 32 DF,  p-value: 1.951e-10
```
Note that `D~structure` is not available for Galician.


We can also examine how the various complexity predictors relate to our morphosemantic measure when their predictive power is combined. Owing to the high correlation between `C_WALS` and `D~structure` entering these both in the model leads to variance inflation, and so we report the models separately.

```

Call:
lm(formula = semanticDistanceAll ~ zeroprop_raw + C_WALS + morphCost_plain + 
    morpho_sum, data = .)

Residuals:
    Min      1Q  Median      3Q     Max 
-8.3669 -2.1707 -0.9017  0.8812 17.3917 

Coefficients:
                Estimate Std. Error t value Pr(>|t|)   
(Intercept)      3.21467   10.59685   0.303  0.76394   
zeroprop_raw    -9.54413    9.67362  -0.987  0.33259   
C_WALS          28.02361    9.75824   2.872  0.00785 **
morphCost_plain 51.47191   24.73396   2.081  0.04705 * 
morpho_sum      -0.15915    0.06948  -2.291  0.03002 * 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 5.291 on 27 degrees of freedom
  (5 observations deleted due to missingness)
Multiple R-squared:  0.6189,	Adjusted R-squared:  0.5624 
F-statistic: 10.96 on 4 and 27 DF,  p-value: 2.069e-05


Call:
lm(formula = semanticDifferenceVarAll ~ zeroprop_raw + C_WALS + 
    morphCost_plain + morpho_sum, data = .)

Residuals:
    Min      1Q  Median      3Q     Max 
-6.6785 -1.6880 -0.7444  1.4273  9.7631 

Coefficients:
                Estimate Std. Error t value Pr(>|t|)   
(Intercept)      1.24207    7.27928   0.171  0.86579   
zeroprop_raw    -6.21520    6.64509  -0.935  0.35792   
C_WALS          19.10203    6.70321   2.850  0.00828 **
morphCost_plain 40.78984   16.99046   2.401  0.02352 * 
morpho_sum      -0.06032    0.04773  -1.264  0.21708   
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 3.634 on 27 degrees of freedom
  (5 observations deleted due to missingness)
Multiple R-squared:  0.6653,	Adjusted R-squared:  0.6157 
F-statistic: 13.42 on 4 and 27 DF,  p-value: 3.82e-06


Call:
lm(formula = semanticDistanceAll ~ zeroprop_raw + D_structure + 
    morphCost_plain + morpho_sum, data = .)

Residuals:
   Min     1Q Median     3Q    Max 
-8.214 -2.510 -1.028  2.000 11.961 

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)      0.26570    7.63301   0.035  0.97246    
zeroprop_raw    -6.46721    7.05616  -0.917  0.36646    
D_structure     46.16865    9.49274   4.864 3.17e-05 ***
morphCost_plain 43.11959   20.36216   2.118  0.04233 *  
morpho_sum      -0.17257    0.05592  -3.086  0.00425 ** 
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 4.37 on 31 degrees of freedom
  (1 observation deleted due to missingness)
Multiple R-squared:  0.7265,	Adjusted R-squared:  0.6913 
F-statistic: 20.59 on 4 and 31 DF,  p-value: 2.292e-08


Call:
lm(formula = semanticDifferenceVarAll ~ zeroprop_raw + D_structure + 
    morphCost_plain + morpho_sum, data = .)

Residuals:
   Min     1Q Median     3Q    Max 
-4.868 -1.868 -0.010  1.248  7.333 

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)     -0.79698    5.18227  -0.154   0.8788    
zeroprop_raw    -4.20581    4.79063  -0.878   0.3867    
D_structure     31.99851    6.44489   4.965 2.37e-05 ***
morphCost_plain 34.48667   13.82445   2.495   0.0181 *  
morpho_sum      -0.06920    0.03796  -1.823   0.0780 .  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 2.967 on 31 degrees of freedom
  (1 observation deleted due to missingness)
Multiple R-squared:  0.7744,	Adjusted R-squared:  0.7453 
F-st
```
