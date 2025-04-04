import { Completer, AsyncCompleter, ReadLineOptions } from 'readline';
export interface Options<T extends string | number = string> {
    default?: T;
    input?: ReadLineOptions['input'] & {
        isTTY?: boolean;
    };
    output?: ReadLineOptions['output'] & {
        isTTY?: boolean;
    };
    prompt?: string;
    silent?: boolean;
    timeout?: number;
    edit?: boolean;
    terminal?: boolean;
    replace?: string;
    completer?: Completer | AsyncCompleter;
    history?: string[];
}
export declare function read<T extends string | number = string>({ default: def, input, output, completer, prompt, silent, timeout, edit, terminal, replace, history, }: Options<T>): Promise<T | string>;
//# sourceMappingURL=read.d.ts.map