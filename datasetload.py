from datasets import load_dataset

df=load_dataset('',split='train').to_pandas()
contents = []
for _,row in df.iterrows():
    content = [
        {'content':row.instruction,'role':'user'},
        {'content':row.response,'role':'assistant'},
    ]
    contents.append(content)
df['messages'] = contents

df.to_json(
    "train.jsonl",
    orient="records",
    lines=True,
)
