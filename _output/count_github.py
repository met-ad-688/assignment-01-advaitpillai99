import subprocess

# Define CSV files
files = ["question_tags.csv", "questions.csv"]
count = 0

for file in files:
    try:
        print(f"Processing {file} using optimized grep...")
        
        # Run grep and count matches without storing output
        result = subprocess.run(["grep", "-i", "GitHub", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Count lines directly from stdout
        file_count = result.stdout.count("\n")
        
        print(f"Lines containing 'GitHub' in {file}: {file_count}")
        count += file_count

    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Total lines containing 'GitHub': {count}")

