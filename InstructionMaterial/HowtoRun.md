# TEIKO Technical Exam Project

This project processes cell count data, generates frequency tables and statistical analyses, and sets up a database for querying. It’s designed to run on a Unix-based system (e.g., Linux, macOS).

## Project Structure
- `InstructionMaterial/cell-count.csv`: Input data file.
- `src/part1/ReturnNewTable.py`: Generates cell frequency table (Part 1).
- `src/part2/ReturnBoxPlots.py`: Creates boxplots (Part 2a).
- `src/part2/StatisticalTests.py`: Performs statistical tests (Part 2b).
- `src/part3/DatabaseDesign`: SQL schema and queries (Part 3).
- `OutputFiles/`: Directory for all outputs.

## Prerequisites
- **Python**: With `pandas`, `matplotlib`, `scipy` (`pip install pandas matplotlib scipy`).
- **Git**: To clone the repository (`sudo apt-get install git`).

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/TEIKOTECHNICALEXAM.git
   cd TEIKOTECHNICALEXAM

## Running Instructions
**Run the following in order from the /TEIKOTECHNICALEXAM directory**
1. `python src/part1/ReturnNewTable.py`
2. `python src/part2/ReturnBoxPlots.py`
3. `python src/part2/StatisticTests.py`
