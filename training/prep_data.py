import pandas as pd
import re
import random
import os

def clean_text(text):
    """Removes URLs, special characters, and extra spaces."""
    if not isinstance(text, str):
        return ""
    text = re.sub(r'http\S+\s*', ' ', text)  # Remove URLs
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # Remove punctuation
    text = re.sub(r'[^\x00-\x7f]', r' ', text)  # Remove non-ASCII
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip().lower()

def load_data(folder_path):
    """Finds and loads the resume dataset regardless of extension."""
    files = os.listdir(folder_path)
    # Look for the resume file specifically
    resume_file = next((f for f in files if 'resume' in f.lower()), None)
    
    if not resume_file:
        raise FileNotFoundError("Could not find a resume dataset in data/raw/")
        
    file_path = os.path.join(folder_path, resume_file)
    print(f"Loading {resume_file}...")
    
    if resume_file.endswith('.csv'):
        return pd.read_csv(file_path)
    elif resume_file.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format!")

def main():
    # 1. Load the data dynamically
    df = load_data('data/raw')
    
    # Check if the column is named 'Category' or something else, standardize it
    if 'Category' not in df.columns:
        # Sometimes it's named 'Role' or 'Profile'
        possible_cols = [c for c in df.columns if c.lower() in ['category', 'role', 'profile']]
        if possible_cols:
            df.rename(columns={possible_cols[0]: 'Category'}, inplace=True)
            
    # 2. Clean the data
    print("Cleaning resume text...")
    df['Cleaned_Resume'] = df['Resume'].apply(clean_text)
    
    # 3. Generate Triplets (Anchor JD, Positive Resume, Negative Resume)
    print("Generating training triplets...")
    categories = df['Category'].unique()
    triplets = []
    
    for category in categories:
        positive_resumes = df[df['Category'] == category]['Cleaned_Resume'].tolist()
        negative_resumes = df[df['Category'] != category]['Cleaned_Resume'].tolist()
        
        anchor_jd = f"Looking for a candidate with skills and experience in {category}."
        
        for _ in range(min(50, len(positive_resumes))):
            pos_resume = random.choice(positive_resumes)
            neg_resume = random.choice(negative_resumes)
            triplets.append({
                "anchor": anchor_jd,
                "positive": pos_resume,
                "negative": neg_resume
            })
            
    # 4. Save to processed folder
    triplet_df = pd.DataFrame(triplets)
    output_path = 'data/processed/training_triplets.csv'
    triplet_df.to_csv(output_path, index=False)
    
    print(f"Success! Created {len(triplet_df)} training pairs.")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    main()