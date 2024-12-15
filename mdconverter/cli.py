import click
from pathlib import Path
from .converter import FileConverter
from typing import Optional, Dict

def create_mlm_config(mlm_model: Optional[str]) -> Optional[Dict]:
    return {'model': mlm_model} if mlm_model else None

@click.command()
@click.argument('input_path', type=click.Path(exists=True), required=False)
@click.option('-o', '--output', type=click.Path(), help='Output file path')
@click.option('--mlm-model', help='MLM model name for image descriptions')
def main(input_path: Optional[str], output: Optional[str], mlm_model: Optional[str]) -> None:
    """Convert documents to Markdown. If no input path specified, converts all files from ./input to ./output"""
    converter = FileConverter(mlm_config=create_mlm_config(mlm_model))
    
    if input_path is None:
        converted = converter.convert_folder()
        click.echo(f"Converted {len(converted)} files to markdown format")
        for file in converted:
            click.echo(f"- {file}")
    else:
        input_path_obj = Path(input_path)
        output_path = output or str(input_path_obj.with_suffix('.md'))
        converter.convert_file(input_path, output_path)
        click.echo(f"Converted {input_path} to {output_path}")

if __name__ == '__main__':
    main()
