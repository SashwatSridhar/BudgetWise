# 💰 BudgetWise: Smart Personal Finance with Machine Learning

> Transform your spending habits with AI-powered expense categorization and intelligent budget recommendations

## 🚀 What is BudgetWise?

BudgetWise is an intelligent personal finance tool that combines traditional budgeting wisdom with modern machine learning. Instead of manually categorizing every expense, let AI do the heavy lifting while you focus on making smarter financial decisions.

**Key Features:**
- 🤖 **AI-Powered Categorization**: Automatically classify expenses using Naive Bayes ML model
- 📊 **50/30/20 Rule Implementation**: Smart budget allocation based on proven financial principles
- 🎯 **Dual Approach**: Choose between rule-based keyword matching or ML prediction
- 📈 **Spending Analysis**: Get detailed breakdowns and insights into your financial habits
- 🔍 **Performance Tracking**: Monitor accuracy and category-wise spending patterns

## 🧠 The Science Behind It

### Traditional Approach: Rule-Based Classification
- Uses keyword matching to categorize expenses
- Implements the proven 50/30/20 budgeting rule:
  - **50% Needs**: Housing, utilities, groceries, transportation
  - **30% Wants**: Entertainment, dining, hobbies, subscriptions  
  - **20% Savings**: Investments, emergency fund, debt repayment

### AI Enhancement: Naive Bayes Classification
- Trains on historical expense data to learn spending patterns
- Uses natural language processing to understand expense descriptions
- Provides probabilistic categorization with accuracy metrics
- Continuously improves with more data

## 💻 How It Works

### 1. Rule-Based Budgeting (`budgetWise_ruleBasedApproach.py`)
```python
# Enter your monthly income
income = 5000

# Add your expenses
expenses = ["rent payment", "netflix subscription", "emergency fund deposit"]
amounts = [1500, 15, 500]

# Get automatic categorization and budget analysis
```

### 2. Machine Learning Classification (`budgetWise_naiveBayes.py`)
```python
# Train the model on your expense history
# Predict categories for new expenses
prediction = predict_description("coffee shop purchase")
# Returns: "wants"
```

## 🛠️ Tech Stack

- **Python 3.7+**: Core programming language
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning implementation
  - `CountVectorizer`: Text-to-numerical conversion
  - `MultinomialNB`: Naive Bayes classifier
  - `train_test_split`: Data splitting utilities
- **CSV Dataset**: Training data for expense categorization

## 📦 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/budgetwise.git
cd budgetwise
```

2. **Install dependencies**
```bash
pip install pandas scikit-learn
```

3. **Run the applications**

For rule-based approach:
```bash
python budgetWise_ruleBasedApproach.py
```

For ML-powered categorization:
```bash
python budgetWise_naiveBayes.py
```

## 📊 Sample Output

```
===== BUDGET BREAKDOWN =====

NEEDS CATEGORY:
rent payment: $1500.00
groceries: $400.00
TOTAL NEEDS: $1900.00

WANTS CATEGORY:
netflix subscription: $15.00
dining out: $200.00
TOTAL WANTS: $215.00

SAVINGS CATEGORY:
emergency fund: $500.00
TOTAL SAVINGS: $500.00

===== SUMMARY =====
Total Expenses: $2615.00
Needs: $1900.00 (72.7%)
Wants: $215.00 (8.2%)
Savings: $500.00 (19.1%)

ML Model Accuracy: 0.87
```

## 🎯 Project Goals Achieved

✅ **Automated Expense Categorization**: AI predicts categories from descriptions  
✅ **Budget Rule Implementation**: 50/30/20 rule with real-time calculations  
✅ **Spending Pattern Analysis**: Category-wise breakdowns and percentages  
✅ **Machine Learning Integration**: Naive Bayes classifier with performance metrics  
✅ **User-Friendly Interface**: Terminal-based input with clear output formatting

## 🔮 Future Enhancements

- **Income-Based Recommendations**: ML models that adapt suggestions based on income brackets
- **Anomaly Detection**: Flag unusual spending patterns automatically
- **Personalized Category Weights**: Learn individual preferences over time
- **Web Interface**: Flask/Django frontend for better user experience
- **Data Visualization**: Charts and graphs for spending trends
- **Multiple ML Models**: Compare Random Forest, SVM, and Neural Networks
- **Real-time Bank Integration**: Connect with banking APIs for automatic data import

## 📈 Machine Learning Insights

The project demonstrates several key ML concepts:

- **Text Classification**: Converting expense descriptions to numerical features
- **Model Evaluation**: Accuracy scoring and category-wise performance analysis
- **Train-Test Split**: Proper data splitting for unbiased evaluation
- **Feature Engineering**: Text vectorization using CountVectorizer
- **Probabilistic Classification**: Multinomial Naive Bayes for categorical prediction

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional ML algorithms implementation
- Enhanced data preprocessing
- Feature engineering improvements
- UI/UX enhancements
- More sophisticated budgeting rules

## 🌟 Acknowledgments

- Inspired by the 50/30/20 budgeting rule by Elizabeth Warren
- Built with scikit-learn's robust ML ecosystem
- Thanks to the open-source community for tools and inspiration

---

**Start your journey to financial intelligence today!** 💪

*Made with ❤️ for better financial futures*
