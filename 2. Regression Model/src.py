{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import pylab as pl\n",
    "import numpy as np\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your user voltage 30\n"
     ]
    }
   ],
   "source": [
    "var=int(input(\"Enter your user voltage \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 2)"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=[]\n",
    "if var==5:\n",
    "    df=pd.read_excel(\"Data/Processed_Data.xlsx\",'5kV')\n",
    "else:\n",
    "    if var==10:\n",
    "        df=pd.read_excel(\"Data/Processed_Data.xlsx\",'10kV')\n",
    "    else:\n",
    "        if var==15:\n",
    "            df=pd.read_excel(\"Data/Processed_Data.xlsx\",'15kV')\n",
    "        else:\n",
    "            if var==20:\n",
    "                df=pd.read_excel(\"Data/Processed_Data.xlsx\",'20kV')\n",
    "            else:\n",
    "                if var==25:\n",
    "                    df=pd.read_excel(\"Data/Processed_Data.xlsx\",'25kV')\n",
    "                else:\n",
    "                    if var==30:\n",
    "                        df=pd.read_excel(\"Data/Processed_Data.xlsx\",'30kV')\n",
    "                    else:\n",
    "                        print(\"Invalid Voltage Level\")\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Leakage_Current</th>\n",
       "      <th>Contamination_Rate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.189227</td>\n",
       "      <td>0.0493</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.275283</td>\n",
       "      <td>0.0614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.331895</td>\n",
       "      <td>0.1414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.421850</td>\n",
       "      <td>0.2230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.927570</td>\n",
       "      <td>0.3206</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Leakage_Current  Contamination_Rate\n",
       "0         0.189227              0.0493\n",
       "1         0.275283              0.0614\n",
       "2         0.331895              0.1414\n",
       "3         0.421850              0.2230\n",
       "4         0.927570              0.3206"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df.Leakage_Current,df.Contamination_Rate,color=\"blue\")\n",
    "plt.xlabel(\"Leakage Current\")\n",
    "plt.ylabel(\"Contamination Rate\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.        , 0.18922724, 0.03580695, 0.00677565],\n",
       "       [1.        , 0.275283  , 0.07578073, 0.02086115],\n",
       "       [1.        , 0.331895  , 0.11015429, 0.03655966],\n",
       "       [1.        , 0.42185   , 0.17795742, 0.07507134],\n",
       "       [1.        , 0.92757   , 0.8603861 , 0.79806834]])"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "from sklearn import linear_model\n",
    "train_x=np.asanyarray(df[[\"Leakage_Current\"]])\n",
    "train_y=np.asanyarray(df[[\"Contamination_Rate\"]])\n",
    "\n",
    "poly=PolynomialFeatures(degree=3)\n",
    "train_x_poly=poly.fit_transform(train_x)\n",
    "train_x_poly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Coefficients:  [[ 0.         -2.3690961   7.86442571 -5.63754876]]\n",
      "Intercept:  [0.25075912]\n"
     ]
    }
   ],
   "source": [
    "clf = linear_model.LinearRegression()\n",
    "train_y_ = clf.fit(train_x_poly, train_y)\n",
    "# The coefficients\n",
    "print ('Coefficients: ', clf.coef_)\n",
    "print ('Intercept: ',clf.intercept_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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QHx8PKtXryY1NRUR4dZbb+Vvf/sbVapUoXLlypQrV45rrrmG0qVLU6hQIfLly4eqcvLkSX766SeOHDnC119/zVdffcWOHTtYvHgx06dPB6By5co0adKEjh07Uq1aNXffcB4Xcr2P1qhRQ62LCWMC7/Tp08ybN4+pU6eydu1aAG688UaaNGlCvXr1uOuuuyhWrNgl7UNV2bt3LytWrCAhIYFVq1aRmprK7bffTvfu3enWrRtFihTJjbcTdkTkE1WtkekyKwTGmKzs3r2bMWPGEBsby+nTp7nhhhvo2rUrLVu2pHLlyn7d99GjR4mLi2PatGls2bKF4sWL07t3b5588kmuueYav+47r8mqEKCqIfWoXr26GmP8b/369dq8eXMVEb3sssu0W7duum7dOj137pwreTZt2qStWrVSEdGIiAh97rnn9MSJE65kCUXAFr3A96pfv7SBBsBuYC/wTCbLu+IZVHy783gku21aITDGv7Zs2aIPPvigAlqiRAl97rnnNDk52e1Yv9u9e7e2bdtWAS1durS+8847rhWnUOJKIQDyA18DFYFCwKdAlQzrdAX+nZPtWiEwxj/27Nnz+xdsyZIl9dVXX9VTp065HeuCPv74Y61Tp44CWrduXf3yyy/djhTUsioE/ryhrBawV1X3qepvQBzQzI/7M8ZchJSUFJ577jluvvlmlixZwnPPPce+ffsYNGgQV155pdvxLqhmzZqsWbOGyZMns337dm677TZee+01zp0753a0kOPPQnAtcNBr+pAzL6NWIrJDROaJSPnMNiQiPUVki4hsOXLkiD+yGhOWEhISuPnmmxk+fDjt2rVj7969DBs27JKv/gmUfPny8eijj7Jr1y4aNWrE4MGDadSoEcnJyW5HCyn+LASSybyMlygtAqJU9TbgA2BGZhtS1cmqWkNVa5QunelIa8aYHPjhhx9o1aoVzZo1o3DhwqxevZqZM2dSpkwZt6NdlDJlyjB//nwmTpzI6tWruf3220lMTHQ7VsjwZyE4BHj/wr8OOOy9gqr+pKq/OpNvA9X9mMcYA8ybN+/300CvvPIK27Zt4+6773Y71iUTEXr16sXmzZspWbIkDz74IG+99ZbbsUKCPwvBZqCSiESLSCGgPZDgvYKIlPWabArs8mMeY8LasWPH6NChA23atCEqKoqtW7cyZMiQPNfHzy233MKmTZuo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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df.Leakage_Current,df.Contamination_Rate,color=\"blue\")\n",
    "if var==5:\n",
    "    XX=np.arange(0.04,0.13,0.001)\n",
    "else :\n",
    "    if var==10:\n",
    "        XX=np.arange(0.06,0.18,0.001)\n",
    "    else:\n",
    "        if var==15:\n",
    "            XX=np.arange(0.06,0.30,0.001)\n",
    "        else:\n",
    "            if var==20:\n",
    "                XX=np.arange(0.1,0.35,0.001)\n",
    "            else:\n",
    "                if var==25:\n",
    "                    XX=np.arange(0.15,0.95,0.001)\n",
    "                else:\n",
    "                    if var==30:\n",
    "                        XX=np.arange(0.15,0.95,0.001)\n",
    "yy=clf.intercept_[0]\n",
    "for i in range(1,4,1):\n",
    "    yy=yy+clf.coef_[0][i]*np.power(XX,i)\n",
    "plt.plot(XX,yy,\"black\")\n",
    "plt.xlabel(\"Leakage Current\")\n",
    "plt.ylabel(\"Contamination Rate\")\n",
    "if var==5:\n",
    "    plt.title(\"For 5kV Voltage\")\n",
    "    plt.savefig('plot5.png',dpi=300, bbox_inches='tight')\n",
    "if var==10:\n",
    "    plt.title('for 10kV Voltage')\n",
    "    plt.savefig('Plot10.png',dpi=300,bbox_inches='tight')\n",
    "if var==15:\n",
    "    plt.title('For 15kV Voltage')\n",
    "    plt.savefig('Plot15.png',dpi=300,bbox_inches='tight')\n",
    "if var==20:\n",
    "    plt.title('For 20kV Voltage')\n",
    "    plt.savefig('Plot20.png',dpi=300,bbox_inches='tight')\n",
    "if var==25:\n",
    "    plt.title('For 25kV Voltage')\n",
    "    plt.savefig('Plot25.png',dpi=300,bbox_inches='tight')\n",
    "if var==30:\n",
    "    plt.title('For 30kV Voltage')\n",
    "    plt.savefig('Plot30.png',dpi=300,bbox_inches='tight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
