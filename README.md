# Contamination_Rate_Detection
This is research project done that I done during my last year of my undergraduate study. I was fascinated by the idea of applying machine learning and computer science concepts in electrical engineering specially in high voltage systems.
This project comprised of two main parts->
  1. Established the relationship between leakage current and applied voltage in high voltage systems.
  2. Classification of different contamination rate on insulation based on current values and applied voltage.
  
 # Process
  1. All the current values were sampled values (discrete in nature). One advantage was that as these values were sampled from nearly sinusoidal values, so extracting feature form those values were pretty staright forward(like calculating statistical values).
 2. To establish the relation we just need to plot the leakage current and applied voltage graph and apply some regression algorithms. Optimising the parameters for polynomial regression was the main job here.
 3. For second part I applied bunch of different machine learning algorithms such as K-nearest Neighbour, Random Forest, Decision Tree, Naive Bayes. Depends on the accuracy KNN was the best suited algorithm in this case.
 
# Tools Used
 1. Python Jupyter Notebook
 2. Python Machine Learning Libraries (Numpy, Pandas)
 3. Machine Learning Algorithms( KNN, Naive Byes, etc)
