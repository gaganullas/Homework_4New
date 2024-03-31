# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Same individual can satisfy multiple rules simultaneously , For example If an individual is a Home Owner (Yes) and also has a Single Marital Status, both rules  Home Owner = Yes  will give DB=Yes and Marital Status = Single will give DB = Yes."
    answers["(b) explain"] = "It does not cover all possible combinations of attribute values, leaving some cases unaddressed, For example Marital Status = Divorced is not covered."
    answers["(c) explain"] = "If a person is not a homeowner and is single, both Home Owner = No, Marital Status = Single and Marital Status = Single rules will yield DB = Yes. Thus, ordering might be necessary for this set of rules."
    answers["(d) explain"] = "If a person is neither a home owner nor single, there are no rules to assign the DB value. Therefore, a default class is needed to handle such instances."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes" 
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Mutually exclusive because they classify distinct categories like birds, fishes, mammals, and reptiles, each based on specific combinations of attributes."
    answers["(b) example"] = "Salamander would not receive classification under the rules R1,R2,R3 and R4."
    answers["(c) example"] = "Each rule (R1,R2,R3,R4) assigns a distinct group without any overlap . Therefore, the order in which these rules are applied does not impact the classification result."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "Gradients are propagated backward from the output layer to the input layer, and the gradients of weights at the k+1th layer can be computed using the gradients of weights at the kth layer via the chain rule."
    answers["(b) explain"] = "When you consider feedforward neural network, during the forward pass, the activations at nodes in layer k+1  are computed based on the activations at nodes in layer k by applying activation functions and weights."
    answers["(c) explain"] = "Vanishing gradient problem is when gradients are propagated backward through the network during the training process, they diminish in magnitude as they pass through each layer. It is not related to the discrepancy between training and test errors."
    answers["(d) explain"] = "If the ANN perfectly classifies all training instances, it means the loss function has reached a minimum, but the gradients of the loss with respect to the weights may not be exactly zero, they might be very small."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.38

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "Choosing k=5 strikes a good balance. It helps smooth out noise and outliers without losing too much local detail, unlike k=1. Also, k=5 prevents oversmoothing, which can happen with larger k values like k=50."
    answers["(b) explain"] = "There is overlap between the two categories of data, so using a large k value like 50 isn't needed, as it might introduce errors and over smoothing effect could result in a loss of discrimination between classes, especially in regions where the classes are densely packed."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "P(A=1,+) = 3 , P(+) = 5 so P(A=1|+) is 0.6"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "Naive Bayes of P(A=1|+)* P(B=1|+)* P(C=1|+) is 0.192 whereas for P(A=1|-)* P(B=1|-)* P(C=1|-) it is 0.032"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] = "P(A=1|B=1+) is not equal to P(A=1|+)"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
