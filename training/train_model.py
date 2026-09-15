import pandas as pd
from sentence_transformers import SentenceTransformer, InputExample
# Updated import path to silence the warning
from sentence_transformers.sentence_transformer.losses import TripletLoss
from torch.utils.data import DataLoader
import os

def main():
    print("1. Loading the training data...")
    df = pd.read_csv('data/processed/training_triplets.csv')
    
    print("2. Preparing data for the model...")
    train_examples = []
    for _, row in df.iterrows():
        train_examples.append(InputExample(texts=[str(row['anchor']), str(row['positive']), str(row['negative'])]))
        
    train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)
    
    print("3. Loading base model (all-MiniLM-L6-v2)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    print("4. Configuring the Loss Function...")
    train_loss = TripletLoss(model=model)
    
    print("5. Starting Fine-Tuning (this might take a few minutes)...")
    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=1,
        warmup_steps=10,
        show_progress_bar=True
    )
    
    print("6. Saving the fine-tuned model...")
    output_dir = 'models/fine_tuned_matcher'
    os.makedirs(output_dir, exist_ok=True)
    model.save(output_dir)
    print(f"Success! Model saved to {output_dir}")

if __name__ == "__main__":
    main()